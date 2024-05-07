# 단어장을 불러와 랜덤으로 저장된 단어 퀴즈 맞히기

from random import *

vocabulary = open("vocabulary.txt","r")

data = {}
i = 0

for line in vocabulary:
    key_value = line.strip().split(":")
    if len(key_value) == 2:
        data[key_value[0]] = key_value[1].strip()

quiz = list(data.keys())
meaning = list(data.values())

while True:
    i = randint(0,len(quiz)-1)
    answer = input(f"{meaning[i]} : ")
    if quiz[i] == answer:
        print("맞았습니다!")
    elif answer == "q":
        break
    else:
        print(f"아쉽습니다. 정답은 {quiz[i]}입니다.")