# Akinator-python
AkinatorAPI ラッパー！
### >>```pip install akinator-python```<<
## 使い方
モジュールをインストールしてexample_jaを実行します  
#### example_ja.py
```py
from akinator_python import Akinator

akinator=Akinator()
print(akinator.start_game())
while True:
    ans=input("回答：")
    if ans=="b":
        print(akinator.go_back()['question'])
    else:
        response=akinator.post_answer(ans)
        if "id_proposition" in response:
            print(f"{response['name_proposition']} / {response['description_proposition']}")
            ans=input("正しいですか？：")
            if ans=="n":
                print(akinator.exclude()['question'])
            elif ans=="y":
                break
        else:
            print(response['question'])
```
Akinator-pythonを使う必要最低限のコードです  
ターミナルで実行して結果を見ることができます  
![0](images/1.png)  
## もう少し知る
```Akinator()```  
- 引数に言語、テーマ、チャイルドモードを設定できます  
- ```language=str```, この引数からエンドポイントのURLが決まります  
  なにも入れないと ```lang=jp``` で日本語が選択されます  
- ```theme=str```, ```characters``` or ```objects``` or ```animals```  
  テーマはデフォルトで ```theme=characters``` キャラクターが選ばれます
- ```child_mode=bool```  
  デフォルトは ```False```
  
```Akinator.post_answer()```  
- ```answer=str```  
  回答は はい : ```y``` いいえ : ```n``` わからない : ```idk``` たぶんそう : ```p``` たぶん違う : ```pn``` の中から選びます
- dictが返ってきます  
  ```
  {'completion': 'OK', 'akitude': 'serein.png', 'step': '1', 'progression': '0.00000',
   'question_id': '464', 'question': 'Is your character a girl?'}
  ```
  
```Akinator.go_back()```  
- 1つ前の質問に戻ります

```Akinator.exclude()```  
- アキネーターの出した答えが間違っている場合、質問を再開できます
### アキネーターが答えを出した時
```
{'completion': 'OK', 'id_proposition': '309720', 'id_base_proposition': '10657795', 'valide_contrainte': '1',
 'name_proposition': 'Arihara Nanami', 'description_proposition': 'Riddle Joker', 
 'flag_photo': '2', 'photo': 'https://photos.clarinea.fr/BL_2_en/600/partenaire/p/10657795__894179331.png', 'pseudo': 'MrSand', 'nb_elements': 1}
```
キャラクター名、画像URLなどの情報がdictで返ってきます  
## コンタクト  
Discord サーバー / https://discord.gg/aSyaAK7Ktm  
Discord ユーザー名 / .taka.  
