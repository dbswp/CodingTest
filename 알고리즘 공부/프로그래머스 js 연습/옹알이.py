babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"];
babbling1 = ["aya", "yee", "u", "maa", "wyeoo"];
baby = ["aya", "ye", "woo", "ma"];

cnt = 0
arr = []
arr1 = []

for i in babbling:
  for j in baby:  # baby와 babbling 비교
    if j in i: # 연속적인 배열 없는 경우
      i=i.replace(j, '1') # babbling[i]의 baby값이 있으면 순서대로 '1'로 변환
  print([i])
  if i.replace('1',''): # 문자 '1' 공백처리
    arr1.append(i)
    continue
  else: #1로 이루어진 경우 cnt값 증가
    cnt += 1
    arr.append(i)

print(arr1)
print(arr)
print(cnt)
print("hello world")
