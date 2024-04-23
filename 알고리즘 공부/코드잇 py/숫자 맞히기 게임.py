import random

randomnumber = random.randint(1,20)

for i in range(4,0,-1):
    num = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if num == randomnumber:
        print(f"축하합니다. {4-i}번만에 숫자를 맞히셨습니다.")
        break
    elif num > randomnumber:
        print("Down")
    else:
        print("Up")
    
print(randomnumber)