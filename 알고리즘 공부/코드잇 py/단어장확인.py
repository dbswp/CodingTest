# 문제 data를 가져와서 질문에 대한 대답도 input()으로 받았고
# enter를 한번 더 입력받아야 정답이 나옴

with open("vocavulary.txt", "r", encoding="UTF-8") as file:
    for word in file:
      data = word.strip().split(":")
      ques = input(f"{data[0]}: ")
      answer = data[1]
      if ques != answer:
        print(f"아쉽습니다. 정답은 {data[1]}입니다.")
      else:
        print("맞았습니다!")
      
