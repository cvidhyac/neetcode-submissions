from typing import List
from copy import deepcopy


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    a_1d_list = [value] * cols
    a_2d_list = [deepcopy(a_1d_list)] * rows
    return a_2d_list


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
