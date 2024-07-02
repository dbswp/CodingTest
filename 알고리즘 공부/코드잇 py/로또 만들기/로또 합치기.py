def count_matching_numbers(numbers, winning_numbers):
    cnt = 0
    # 지난 실습의 코드를 여기에 붙여 넣으세요
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

# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))