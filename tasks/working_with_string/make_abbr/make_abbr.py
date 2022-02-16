def make_abbr(words: str) -> str:
    # write your code here
    if words == '':
        return ''
    list_words = words.split(' ')
    abbr = ''
    for word in list_words:
        abbr += word[0].upper()
    return abbr
