t = int(input())
for i in range(1,t+1):
  n = int(input()) #테스트 케이스 번호
  score =  list(map(int, input().split())) 
  counter = {}
  for value in score:
      if value in counter:
          counter[value] += 1
      else:
          counter[value] = 1
  max_key = max(counter, key=counter.get)
  print(f"#{i} {max_key}")
