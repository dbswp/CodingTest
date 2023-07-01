from collections import Counter
def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    answer = a - b
    for key in answer.keys():
        return key, a

# Counter -> {'A': 2, 'B': 1, 'C': 1}
# answer = a - b
# {'A': 1}


# def solution(participant, completion):
# 	answer = {}
# 	for i in participant:
# 		  if i in answer:
# 		     answer[i] += 1
# 		  else:
# 		     answer[i] = 1
# 	for i in completion:
#       if answer[i]==1: 
#           del answer[i]
#       else: 
#             answer[i] -=  1
# 	for key in answer.keys():
# 	    return key