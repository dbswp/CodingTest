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

def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    cnt = 0
    for i in numbers:
        for j in winning_numbers:
            if i == j:
                cnt += 1
    return cnt

def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    # 보너스 번호도 같이 비교하기 위해 슬라이싱으로 나눔
    cnt = count_matching_numbers(numbers,winning_numbers[:6])
    bonuse_cnt = count_matching_numbers(numbers, winning_numbers[6:])
    if cnt == 6:
        return 1000000000
    elif cnt == 5 and bonuse_cnt == 1:
        return 50000000
    elif cnt == 5:
        return 1000000
    elif cnt == 4:
        return 50000
    elif cnt == 3:
        return 5000
    else:
        return 0