from math import floor


def split_string(string: str) -> list:
    # write your code here
    if len(string) % 2 == 1:
        string += '_'
    list_split_string = []
    new_string = string
    for i in range(floor(len(string) / 2)):
        list_split_string.append(new_string[:2])
        new_string = new_string[2:]
    return list_split_string
