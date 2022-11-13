#1 거스름돈 계산

# n = int(input())
# coin = [500,100,50,10]
# cnt = 0

# for i in coin:
#     cnt += n//i
#     n = n % i
#     if n < 0:
#         break
# print(cnt)
# ----------------------------------

#2 1이 될때까지 반복

# n,k = map(int, input().split())
# cnt = 0
# for i in range(n):
#     if n % k == 0:
#         n = n // k
#         cnt += 1
#         if n == 1:
#             break
#     else:
#         n = n - 1
#         cnt += 1
#         if n == 1:
#             break
# print(cnt)
# ----------------------------------

#3 곱하거나 더하기 문제

# n = input()
# result = int(n[0])
# for i in range(1,len(n)):
#     num = int(n[i])
#     if num <=1 or result <=1:
#         result += num
#     else:
#         result *= num
# print(result)
# ----------------------------------

#4 모험가 길드
n = int(input())
alist = list(map(int, input().split()))
alist.sort()
cnt = 0 # 현재 그룹에 포함된 모험가의 수
res = 0 # 총 그룹의 수
for i in alist:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
print(res)
