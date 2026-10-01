from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    count_dict = defaultdict(int)
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    num_dict = defaultdict(list)
    for num_list in nums:
        key = num_list[0]
        num_dict[key].extend(num_list[1:])
    return num_dict


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
