from akinator_python import Akinator

akinator=Akinator(lang="en")
print(akinator.start_game())
while True:
    ans=input("answer：")
    if ans=="b":
        print(akinator.go_back()['question'])
    else:
        response=akinator.post_answer(ans)
        if "id_proposition" in response:
            print(f"{response['name_proposition']} / {response['description_proposition']}")
            ans=input("is it correct?：")
            if ans=="n":
                print(akinator.exclude()['question'])
            elif ans=="y": 
                break
        else:
            print(response['question'])