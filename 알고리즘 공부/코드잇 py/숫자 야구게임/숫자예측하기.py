def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    i = 0
    # 여기에 코드를 작성하세요
    while len(new_guess) < 3:
        i += 1
        num = int(input(f"{i}번째 숫자를 입력하세요: "))
        if num <= 9 and num >= 0:
            new_guess.append(num)
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            i -= 1
    return new_guess
    
    
# 테스트 코드
print(take_guess())


## new_guess의 길이를 i번째 로 변환
# 중복되거나 범위를 벗어나지 않으면 길이가 늘어나지 않기때문에 좋은 방법!
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess
  
    
# 테스트 코드
print(take_guess())