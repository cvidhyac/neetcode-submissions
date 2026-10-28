import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    popped_list = []
    as_min_heap = heap.copy()
    heapq.heapify(as_min_heap)

    while as_min_heap:
        popped_list.append(heapq.heappop(as_min_heap))
    return popped_list



# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
