# open()로 지정된 파일 읽기 as 이름 정의
# strip()를 사용하면 화이트스페이스(앞 뒤 공백 삭제 가능)


with open('코드잇 py/chicken.txt', 'r' , encoding='UTF-8') as f:
    for line in f:
        print(line.strip())