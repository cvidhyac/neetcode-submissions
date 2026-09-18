def remove_fourth_character(word: str) -> str:
    word_upto_three = word[0:3]
    word_beyond = word[4:]
    return word_upto_three + word_beyond


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
