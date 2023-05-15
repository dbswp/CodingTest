def solution(num_list):
    answer = 0
    plus = 0
    mul = 1
    for i in num_list:
        if len(num_list) >= 11:
            plus += i
            answer = plus
        elif len(num_list) <= 10:
            mul *= i
            answer = mul
    return answer