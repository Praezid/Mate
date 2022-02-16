def get_success_rate(statistics: str) -> int:
    # write your code here
    count = 0
    for item in statistics:
        if int(item) == 1:
            count += 1
    return round(100 * count / len(statistics))
