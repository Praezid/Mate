description_declare_variables = """The is_special_number function takes a number and must determine whether it is special or not.
A number is said to be special if it includes only 0, 1, 2, 3, 4 or 5.
The is_special_number function should return the string 'Special !!' if the number is special, and 'NOT !!' if it is not.
Notes:
    The number passed to the function is positive (n> 0).
    All one-digit numbers in the range [0: 5] are considered special numbers.
Examples:
    is_special_number (2) == 'Special !!'
    
    2 is a one-digit number in the range [0: 5].
    is_special_number (9) == 'NOT !!'
    
    although 9 is a one-digit number, it is not in the range [0: 5].
    is_special_number (23) == 'Special !!'
    
    all digits of the number 23 are in the interval [0: 5].
    is_special_number (39) == 'NOT !!'
    
    although there is a number 3, which is in the interval,    but the second number (9) is not in it
    Note: each digit must be in the interval [0: 5]."""
