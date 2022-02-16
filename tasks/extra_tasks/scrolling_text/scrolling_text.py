def scrolling_text(string: str) -> list:
    # write your code here
    scroll_list = []
    for i in range(len(string)):
        scroll_list.append(string.upper())
        string = string[1:] + string[:1]
    return scroll_list
