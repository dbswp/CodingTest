n = int(input())
for i in range(1, n+1):
    count = 1
    a = list(input())
    if a[0] == a[i]:
        break
    else:
        count += 1
    print("#"+str(i),count)