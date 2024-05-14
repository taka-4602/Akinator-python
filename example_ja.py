from akinator_python import Akinator

akinator=Akinator()
akinator.start_game()
while True:
    try:
        print(akinator.question)
        ans=input("回答：")
        if ans=="b":
            akinator.go_back()
        else:
            akinator.post_answer(ans)
            if akinator.answer_id:
                print(f"{akinator.name} / {akinator.description}")
                ans=input("正しいですか？：")
                if ans=="n":
                    akinator.exclude()
                elif ans=="y":
                    break
                else:
                    break
    except Exception as e:
        print(e)
        continue
