#1 상하좌우

# n = int(input())
# p = input().split()
# x,y = 1, 1

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move = ['L','R','U','D']

# for i in p:
#     for j in range(len(move)):
#         if i == move[j]:
#             nx = x + dx[j]
#             ny = y + dy[j]
#     if nx<1 or ny<1 or nx>n or ny>n:
#         continue
#     x,y = nx,ny
# print(x,y)

#2 시간 문제
n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1
print(cnt)