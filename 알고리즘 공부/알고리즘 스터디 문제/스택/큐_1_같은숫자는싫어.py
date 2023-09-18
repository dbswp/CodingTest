def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer

# 처음 풀이
# def solution(arr):
#     answer = []
#     for i in arr:
#         if i in arr:
#             continue
#         else:
#             answer.append(i)
#     return answer