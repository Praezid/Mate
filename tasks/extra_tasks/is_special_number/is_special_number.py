def is_special_number(number: int) -> str:
    # write your code here
    if 0 <= number <= 5:
        return 'Special!!'
    for item in str(number):
        if int(item) == 6 or int(item) == 7 or int(item) == 8 or int(item) == 9:
            return 'NOT!!'
    return 'Special!!'
