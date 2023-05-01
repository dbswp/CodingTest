# def solution(num_list):
#     answer = [None] * len(num_list)
#     index = 0
#     for n in num_list:
#         for i in range(2, n-1):
#             if(n%i == 0):
#                 answer[index] = False
#                 break
                
#         if answer[index] == None:
#             answer[index] = True
            
#         index += 1
        
#     return answer