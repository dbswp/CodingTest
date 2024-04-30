# 여기에 코드를 작성하세요
with open("코드잇 py/chicken.txt", "r", encoding='UTF-8') as f:
    total = 0 
    cnt = 0
    for data in f:
        chicken = data.strip().split(": ")
        # date = chicken[0][:2]
        price = chicken[1]
        total += int(price)
        cnt += 1
    avg = total / cnt
    
    print(avg)
    # if date != 31:
    #     print(total / 30)
    # else:
    #     print(total / 31)
