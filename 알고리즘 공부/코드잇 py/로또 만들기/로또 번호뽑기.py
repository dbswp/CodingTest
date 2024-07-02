from random import randint
# 1번재 방법
# 위에 방법은 공 6개를 먼저 뽑아 정리 후 추가 공 뽑기 
def generate_numbers(n):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    num_list = []
    while len(num_list) < n:
        num = randint(1,45)
        
        if num not in num_list:
            num_list.append(num)
            num_list.sort()
    
    plusnumber = randint(1,45)
    if plusnumber not in num_list:
        num_list.append(plusnumber)
            
    return num_list


def draw_winning_numbers():
    # 여기에 코드를 작성하세요
    return generate_numbers(6)

# 2번째 방법 
# 아래 방법은 공 7개를 뽑고 0~5까지 정렬 후 6번째 공을 추가로 더해준
# def generate_numbers(n):
#     num_list = []
    
#     while len(num_list) < n:
#         num = randint(1,45)
#         if num not in num_list:
#             num_list.append(num)
#     return num_list
    
# def draw_winning_numbers():
#     numbers = generate_numbers(7)
#     return sorted(numbers[:6]) + numbers[6:]
# 테스트 코드
print(draw_winning_numbers())