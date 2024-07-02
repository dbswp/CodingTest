from random import randint


def generate_numbers(n):
    # 여기에 코드를 작성하세요
    num_list = []
    while len(num_list) < n:
        num = randint(1,45)
        
        if num not in num_list:
            num_list.append(num)
    return num_list

# 테스트 코드
print(generate_numbers(6))