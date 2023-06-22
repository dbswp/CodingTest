def solution(priorities, location):
    answer = 0
    idxArr = [i for i in range(len(priorities))]
    max_priorities = max(priorities)
    
    while len(priorities) != 0:
        if priorities[0] < max_priorities:
            priorities.append(priorities.pop(0))
            idxArr.append(idxArr.pop(0))
        else:
            answer += 1
            priorities.pop(0)
            if idxArr.pop(0) == location:
                return answer
            max_priorities = max(priorities)