from collections import Counter
def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    answer = a - b
    for key in answer.keys():
        return key
      
#     for i in participant:
#         if i in answer:
#             answer[i] += 1
#         else:
#             answer[i] = 1
    
#         for j in completion:
#             if j in answer:
#                 answer[j] -= 1
#     return answer