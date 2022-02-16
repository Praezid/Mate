def is_jumping(number: int) -> str:
    # write your code here
    if len(str(number)) == 1:
        return 'JUMPING'
    string = str(number)
    for i in range(len(string) - 1):
        if abs(int(string[i]) - int(string[i + 1])) > 1 or abs(int(string[i]) - int(string[i + 1])) == 0:
            return 'NOT JUMPING'
    return 'JUMPING'

