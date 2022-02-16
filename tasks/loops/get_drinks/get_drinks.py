def get_drinks(number_of_guests: int) -> int:
    # write your code here
    count_of_drinks = 0
    for i in range(number_of_guests + 1):
        count_of_drinks += i
    return count_of_drinks
