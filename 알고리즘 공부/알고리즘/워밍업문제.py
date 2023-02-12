# 1부터 10,000까지 8이라는 숫자가 몇번 나오는지 8808 = 3!!

str(list(range(1,10001))).count('8')
str([i for i in range(10001)]).count('8')

count = 0
for i in range(10001):
    if '8' in str(i):
        count += str(i).count('8')
print(count)


# 1차원의 점들이 주어졌을때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수

s = [1,3,4,8,13,17,20,30]
m = max(s)
print(m)
index = 0
for i in range(len(s)-1):
    if m > s[i+1] - s[i]:
        index = i
        m = s[i+1] - s[i]
print((s[index], s[index+1]))