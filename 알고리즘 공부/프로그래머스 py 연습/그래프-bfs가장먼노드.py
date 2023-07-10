from collections import deque

def solution(n, edge):
    # bfs는 큐 자료구조 이용
    # 빈 그래프 만들기
    graph = [[] for _ in range(n+1)]
    # 방문을 확인하는 배열 확인은 0으로 초기화 후 방문하면 바꿔주기
    visited = [0] * (n+1)
    
    # 그래프의 노드간 연결을 위해 인접 리스트에 서로 추가해줘야함
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    # 출발한 노드 1
    q = deque([1])
    # 출발 노드의 최단거리를 0으로
    visited[1] = 1
    
    while q:
        now = q.popleft() # 현재노드
        # 이동 가능한 모든 노드 확인
        for i in graph[now]:
            # if visited[i] == 0
            if not visited[i]: # 방문하지 않았으면
                q.append(i) # 큐에 추가
                visited[i] = visited[now] + 1 # 최단 거리 갱신
                
    max_v = max(visited)
    cnt = visited.count(max_v)
    return cnt