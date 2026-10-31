import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    as_min_heap = [(-num, num) for num in nums]
    heapq.heapify(as_min_heap)
    rev_sort = []
    while as_min_heap:
        rev_sort.append(heapq.heappop(as_min_heap)[1])
    return rev_sort


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
