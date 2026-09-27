from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    rotated_deq = deque()

    append_to_deq = arr[:k]
    sliced_rem_list = arr[k:]
    for i in sliced_rem_list:
        rotated_deq.append(i)
    for i in append_to_deq:
        rotated_deq.append(i)
    return rotated_deq





# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0)) # 1 2 3 4 5
print(rotate_list([1, 2, 3, 4, 5], 1)) # 5 1 2 3 4
print(rotate_list([1, 2, 3, 4, 5], 2)) # 4 5 1 2 3
print(rotate_list([1, 2, 3, 4, 5], 3)) # 3 4 5 1 2
print(rotate_list([1, 2, 3, 4, 5], 4)) 
print(rotate_list([1, 2, 3, 4, 5], 5))
