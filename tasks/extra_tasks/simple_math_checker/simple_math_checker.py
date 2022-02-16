def check_number(number: int) -> list:
    # write your code here
    result_list = []
    if number > 0:
        result_list.append(True)
    else:
        result_list.append(False)
    if number % 2 == 0:
        result_list.append(True)
    else:
        result_list.append(False)
    if number % 10 == 0:
        result_list.append(True)
    else:
        result_list.append(False)
    return result_list
