def can_buy_beer(age: int) -> str:
    # write your code here
    response = ''
    if age < 18:
        response = 'You can not buy beer'
    else:
        response = 'You can buy beer'
    return response
