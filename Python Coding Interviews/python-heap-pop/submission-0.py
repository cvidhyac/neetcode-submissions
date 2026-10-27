import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    popped_list = []
    as_min_heap = []
    for item in heap:
        heapq.heappush(as_min_heap, item)

    while as_min_heap:
        item = heapq.heappop(as_min_heap)
        popped_list.append(item)
    return popped_list



# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
