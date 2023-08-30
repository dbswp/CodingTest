import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# dfs 정의
def dfs(x, y): # 상, 하, 좌, 우 방향 설정
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]

		# 네 방향으로 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
				# nx와 ny의 범위 안에 있고, 배추면(1) 지나간 길을 -1로 변경하고 탐색 시작
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1: 
# graph[ny][nx] 는 실제 그래프에서 (가로,세로)를 2차원 배열의 (행,열) 순으로 바꾸기 위함 
            graph[ny][nx] = -1
            dfs(nx, ny)

t = int(input()) # 테스트 케이스 입력
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

		# 배추 위치 표시
		# graph[Y][X] 는 실제 그래프에서 (가로,세로)를 2차원 배열의 (행,열) 순으로 바꾸기 위함 
    for _ in range(k):
        X, Y = map(int, input().split()) 
        graph[Y][X] = 1 

    count = 0
    for a in range(m): # 더 이상 1이 존재하지 않으면 count + 1 하여 개수 구하기
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a ,b)
                count += 1
    print(count)