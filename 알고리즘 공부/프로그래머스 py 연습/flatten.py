for tc in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))
    
    for i in range(n):
        max_box = max(box)
        min_box = min(box)
        max_index = box.index(max_box)
        min_index = box.index(min_box)
        box[max_index] -= 1
        box[min_index] += 1
    print(f"#{tc} {max_box - min_box}")
    
    
# for t in range(1, 11) :
#     N = int(input())
#     box = list(map(int, input().split()))

#     for i in range(N) :
#         max_index = box.index(max(box))
#         min_index = box.index(min(box))
#         box[max_index] -= 1
#         box[min_index] += 1

#     print("#{} {}".format(t, max(box)-min(box)))

# 최저 높이의 상자 인덱스 위치 반환
# def min_search():
#     min_value = 101
#     min_idx = -1

#     # 최저 높이 찾기
#     for i in range(len(box_lst)):
#         if box_lst[i] < min_value:
#             min_value = box_lst[i]
#             min_idx = i
#     return min_idx

# # 최고 높이의 상자 인덱스 위치 반환
# def max_search():
#     max_value = 0
#     max_idx = -1

#     # 최고 높이 찾기
#     for i in range(len(box_lst)):
#         if box_lst[i] > max_value:
#             max_value = box_lst[i]
#             max_idx = i
#     return max_idx

# for tc in range(1, 10+1):
#     N = int(input())  # 덤프횟수
#     box_lst = list(map(int, input().split()))

#     # N번 덤프하기
#     for i in range(N):
#         # 최고 높이 상자 한칸 내리기
#         box_lst[max_search()] -= 1
#         # 최저 높이 상자 한칸 올리기
#         box_lst[min_search()] += 1

#     print("#{} {}".format(tc, box_lst[max_search()] - box_lst[min_search()]))