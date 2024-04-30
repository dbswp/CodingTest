# 인접행렬

# 정점 = n, 간선 = e
n, e = map(int, input().split())
borad = [[0] for i in range(n)]
for i in range(e):
  u, v = map(int, input().split())
  
  # 양방향 그래프이기 때문에 간선이 서로 연결이 되게
  borad[u][v]
  borad[v][u]
  
print(borad)

# 인접리스트
