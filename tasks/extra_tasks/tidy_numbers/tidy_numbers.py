def is_tidy(number: int) -> bool:
    # write your code here
    list_numbers = []
    for item in str(number):
        list_numbers.append(item)
    list_numbers = sorted(list_numbers)
    new_number = ''
    for item in list_numbers:
        new_number += item
    if int(new_number) == number:
        return True
    else:
        return False