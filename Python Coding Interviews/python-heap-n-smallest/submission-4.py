import heapq
from typing import List


def create_min_heap(arr: List[int]) -> List[int]:
    min_heap = arr.copy()
    heapq.heapify(min_heap)
    return min_heap

def get_min_element(arr: List[int]) -> int:
    min_heap = create_min_heap(arr)
    return min_heap[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    min_heap = create_min_heap(arr)
    return heapq.nsmallest(4, min_heap)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    min_heap = create_min_heap(arr)
    return sorted(heapq.nsmallest(2, min_heap), reverse=True)


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

