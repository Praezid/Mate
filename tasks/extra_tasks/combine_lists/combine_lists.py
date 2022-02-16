def combine_lists(ls1: list, ls2: list) -> list:
    # write your code here
    combine_list = []
    for i in range(len(ls1)):
        combine_list.append(ls1[i] + ls2[i])
    return combine_list
