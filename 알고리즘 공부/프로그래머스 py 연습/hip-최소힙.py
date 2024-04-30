import heapq
import sys

read = sys.stdin.readline

N = int(input())

nums = []

for _ in range(N):
  x = int(read())
  if x==0:
    if nums:
      print(heapq.heappop(nums))
    else:
      print(0)
      
  else:
    heapq.heappush(nums,x)