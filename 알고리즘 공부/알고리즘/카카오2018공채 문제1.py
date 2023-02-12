#이진수로 변경(bin(i | j)), 자리수 채우기(zfill), 배열 합치기(zip)

def solution(n,arr1,arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        answer.append(bin(i|j)[2:].zfill(n).replace('1','#').replace('0',' '))
    return answer

testcase = [(5,[9,20,28,18,11],[30,1,21,17,28])]

for i,j,k in testcase:
    print(solution(i,j,k))