# 스택은 테이터의 삽입과 삭제가 데이터의 가장 한쪽 끝에서만 이러나는 자료구조.
# 후입선출 - 가장 마지막에 삽이된 데이터가 가장 먼저 사용되거나 삭제.

class stack:
    def __init__(self):
        self.items = [] #스택 객체 생성
    def push(self,item):
        self.items.append(item) #스택 객체에 item요소 추가
    def pop(self):
        return self.items.pop() # 스택 요소 삭제
    def peek(self): #스택 맨 앞요소로 리턴
        return self[0]
    def isEmpty(self): # 스택이 비었는지 확인
        return not self.items

stk = stack()
print(stk)
print(stk.isEmpty())
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(2)
print(stk.items)
print(stk.pop())
print(stk.isEmpty())
print(stk.pop())
