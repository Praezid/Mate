description_declare_variables = """Implement the is_jumping function, which takes the number number and returns the JUMPING
string if each digit in the number differs from the next one by 1. If the condition is not met, the NOT JUMPING string.
Notes:
    The input number is always positive
    The difference between 9 and 0 is not considered as 1
    All numbers that consist of one digit - JUMPING
Examples:
    is_jumping(9) == 'JUMPING'
    It's single-digit number
    
    is_jumping(79) == 'NOT JUMPING'
    Adjacent digits don't differ by 1
    
    is_jumping(23454) == 'JUMPING'
    Adjacent digits differ by 1"""