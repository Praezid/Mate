from math import floor


def get_speed_statistic(test_results: list) -> list:
    # write your code here
    if test_results == []:
        return [0, 0, 0]
    return [min(test_results), max(test_results), floor(sum(test_results) / len(test_results))]
