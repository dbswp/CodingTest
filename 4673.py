a = []
for n in range(1, 10001):
    if n < 10:
        n = n + n
        a.append(n)
    elif n < 100:
        n = n + (n//10) + (n%10)
        a.append(n)
    elif n < 1000:
        n = n + (n//100) + ((n%100)//10) + ((n%100)%10)
        a.append(n)
    elif n <= 10000:
        n = n + (n//1000) + ((n%1000)//100) + (((n%1000)%100)//10) + (((n%1000)%100)%10)
        a.append(n)

for i in range(1,10001):
    if i in a:
        pass
    else:
        print(i)