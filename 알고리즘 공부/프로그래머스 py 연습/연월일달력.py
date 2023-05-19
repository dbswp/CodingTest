T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    ymd = str(input())
    year = ymd[0:4]
    month = ymd[4:6]
    day = ymd[6:]
    days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if 0 < int(month) <13 and int(day) <= days[int(month)]:
        print("#{} {}/{}/{}".format(i,year,month,day))
    else:
        print('#{} {}'.format(i,-1))
