description_declare_variables = """Our server takes a list of robot speeds test_results, passes it through
the `get_speed_statistic` function and returns statistics as a list where:
    the first element is the minimum speed
    the second is the maximum
    third - average speed, rounded down (use the floor function)

Examples:
    get_speed_statistic ([10, 10, 11, 9, 12, 8]) == [8, 12, 10]
    get_speed_statistic ([10]) == [10, 10, 10]
    get_speed_statistic ([]) == [0, 0, 0]
    get_speed_statistic ([8, 9, 9, 9]) == [8, 9, 8]
    get_speed_statistic ([5]) == [5, 5, 5]"""
