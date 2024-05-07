# 파일을 쓸때 "w"로 쓴다.
# 하지만 "a"로 수정과 새로운 문서를 작성 가능

with open("new_file.txt", "a", encoding='UTF-8') as f:
    f.write("hello world!\n")
    f.write("my name is dbswp")