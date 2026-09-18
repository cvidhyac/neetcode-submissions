def concatenate(s1: str, s2: str) -> str:
    concat_op = s1 + s2
    if len(concat_op) > 10:
        return "Too long!"
    else:
        return concat_op




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
