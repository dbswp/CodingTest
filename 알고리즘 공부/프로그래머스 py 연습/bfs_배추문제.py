from collections import deque
T = int(input())
for i in range(T):
  # m=가로, n = 세로
  m, n, k = map(int, input().split())
  borad = [[0]*n for _ in range(m)]

  for i in range(k):
    x,y = map(int, input().split())
    borad[y][x] =1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def Bfs(x,y):
  queue = deque()
  queue.append((x,y))
  
  while(queue):
    x,y = queue.popleft()
    
    