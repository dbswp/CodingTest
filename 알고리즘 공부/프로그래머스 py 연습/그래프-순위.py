# def solution(n, results):
#     answer = 0
#     graph = [[0] * n for _ in range(n)]
#     for p1,p2 in results:
#         graph[p1-1][p2-1] = 1 # p1이 이기면 0 -> 1
#         graph[p2-1][p1-1] = -1 # p2가 이기면 0 -> -1
        
#     # i->j j->k = i->k 공식 만들기 위함
#     # 플로이드-워셜 알고리즘
#     # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if i==j or graph[i][j] in [1,-1]:
#                     continue
#                 if graph[i][k] == graph[k][j] == 1:
#                     graph[i][j] = 1
#                     graph[j][i] = graph[k][i] = graph[j][k] = -1
#     for i in graph:
#         if i.count(0) == 1:
#             answer += 1
#     return answer

def solution(n, results):
    total = [['?' for i in range(n)] for j in range(n)]
    
    # 자신의 노드점은 SELF로 초기화
    for i in range(n):
        total[i][i] = 'SELF'
    
    for p1,p2 in results:
        total[p1-1][p2-1] = 'WIN' # p1이 이기면 ? -> WIN
        total[p2-1][p1-1] = 'LOSE' # p1이 이기면 ? -> LOSE

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WIN' and total[k][j] == 'WIN':
                    total[i][j] = 'WIN'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0
    for i in total:
        if '?' not in i:
            answer += 1

    return answer