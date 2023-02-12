# 큐는 한쪽끝으로 자료를 넣고, 반대쪽에서는 자료를 뺼 수 있는 선형구조
# 선입선출

from collections import deque

a_list = deque('asdfg')
print(a_list)
a_list.append('k')
a_list.appendleft('h')
print(a_list)

class listqueue:
    def __init__(self):
        self.queue = []
    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
    def enqueue(self, n):
        self.queue.append(n)
        pass

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    lq = listqueue()
    lq.enqueue('1')
    lq.enqueue('2')
    lq.enqueue('3')
    lq.enqueue('4')
    lq.enqueue('5')
    lq.printQueue()
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    lq.printQueue()