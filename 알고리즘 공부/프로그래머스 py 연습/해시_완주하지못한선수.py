from collections import Counter
def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    answer = a - b
    for key in answer.keys():
        return key, a
      
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