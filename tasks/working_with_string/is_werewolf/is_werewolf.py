import string


def is_werewolf(target: str) -> bool:
    # write your code here
    for ch in string.punctuation:
        target = target.replace(ch, '')
    target = target.replace(' ', '').upper()
    reverse_target = target[::-1]
    for i in range(len(target)):
        if target[i] != reverse_target[i]:
            return False
    return True
