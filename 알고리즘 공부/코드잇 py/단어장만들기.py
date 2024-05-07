with open("vocavulary.txt", "a", encoding="UTF-8") as f:
    while True:
        ques = input("영어 단어를 입력하세요: ")
        answer = input("한국어 뜻을 입력하세요: ")
        if ques == "q" and answer == "q" :
            break
        f.write(f"{ques}:{answer}\n")
