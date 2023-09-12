import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
hap = [0]
sum = 0

for i in arr:
  sum += i
  hap.append(sum)

for _ in range(m):
  i,j = map(int, sys.stdin.readline().split())
  print(hap[j] - hap[i-1])
  
  
# 처음에는 배열에 저장한 후 구간별로 더하기 구함
# 시간 초과