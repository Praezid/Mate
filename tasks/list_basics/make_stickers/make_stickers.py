def make_stickers(details_count: int, robot_part: str) -> list:
    # write you code here
    if details_count == 0: return []

    stickers = []
    for i in range(1, details_count + 1):
        stickers.append(f"{robot_part} detail #{i}")
    return stickers
