import requests
from bs4 import BeautifulSoup

class AkinatorError(Exception):
    pass
class Akinator():
    def __init__(self,theme:str="characters",lang:str="jp",child_mode:bool=False) -> None:
        self.ENDPOINT=f"https://{lang}.akinator.com/"
        if theme=="characters":
            sid=1
        elif theme=="objects":
            sid=2
        elif theme=="animals":
            sid=14
        else:
            raise AkinatorError("the theme must be characters / objects / animals")
        self.session=requests.session()
        self.progress={
            "step":0,
            "progression":0.0,
            "sid":sid,
            "cm":child_mode,
            "answer":0,
        }

    def start_game(self):
        game=self.session.post(f"{self.ENDPOINT}game",json={"sid":self.progress["sid"],"cm":self.progress["cm"]}).text
        soup = BeautifulSoup(game,"html.parser")
        askSoundlike=soup.find(id="askSoundlike")
        question_label=soup.find(id="question-label").get_text()
        session_id=askSoundlike.find(id="session").get("value")
        signature_id=askSoundlike.find(id="signature").get("value")
        self.progress["session"]=session_id
        self.progress["signature"]=signature_id
        return question_label

    def post_answer(self,answer:str):
        if answer=="y":
            self.progress["answer"]=0
        elif answer=="n":
            self.progress["answer"]=1
        elif answer=="idk":
            self.progress["answer"]=2
        elif answer=="p":
            self.progress["answer"]=3
        elif answer=="pn":
            self.progress["answer"]=4
        else:
            raise AkinatorError("the answer must be y / n / idk / p / pn")
        try:
            progression=self.session.post(f"{self.ENDPOINT}answer",json=self.progress)
            progression=progression.json()
            if progression["completion"]=="KO":
                raise AkinatorError("completion : KO")
            try:
                self.progress["step"]=int(progression["step"])
                self.progress["progression"]=float(progression["progression"])
            except:
                None
            return progression
        except:
            raise AkinatorError(progression.text)

    def go_back(self):
        if self.progress["step"]==0:
            raise AkinatorError("it's first question")
        if "answer" in self.progress:
            del self.progress["answer"]
        try:
            goback=self.session.post(f"{self.ENDPOINT}cancel_answer",json=self.progress)
            goback=goback.json()
            self.progress["step"]=int(goback["step"])
            self.progress["progression"]=float(goback["progression"])
            return goback
        except:
            raise AkinatorError(goback.text)

    def exclude(self):
        if "answer" in self.progress:
            del self.progress["answer"]
        try:
            exclude=self.session.post(f"{self.ENDPOINT}exclude",json=self.progress)
            exclude=exclude.json()
            self.progress["step"]=int(self.progress["step"])
            self.progress["progression"]=float(self.progress["progression"])
            return exclude
        except:
            raise AkinatorError(exclude.text)