from tasks.extra_tasks.list_plus_list import list_plus_list


def test_short_lists():
    assert list_plus_list.get_lists_sum([1, 2], [3, 4]) == 10, (
        "Function 'get_lists_sum' should return 10 "
        "when ls1 is equal to [1, 2] and ls2 is equal to [3, 4]"
    )


def test_0_when_lists_are_empty():
    assert list_plus_list.get_lists_sum([], []) == 0, (
        "Function 'get_lists_sum' should return 0 "
        "when given lists are empty"
    )


def test_lists_with_only_positive_numbers():
    assert list_plus_list.get_lists_sum([1, 2, 9], [3, 3, 3]) == 21, (
        "Function 'get_lists_sum' should return 21 "
        "when ls1 is equal to [1, 2, 9] and ls2 is equal to [3, 3, 3]"
    )


def test_lists_with_only_negative_numbers():
    assert list_plus_list.get_lists_sum([-1, -2, -9], [-3, -3, -3]) == -21, (
        "Function 'get_lists_sum' should return -21 "
        "when ls1 is equal to [-1, -2, -9] and ls2 is equal to [-3, -3, -3]"
    )


def test_lists_with_positive_and_negative_numbers():
    assert list_plus_list.get_lists_sum([-1, 1, 9], [3, -3, -3]) == 6, (
        "Function 'get_lists_sum' should return 6 "
        "when ls1 is equal to [-1, 1, 9] and ls2 is equal to [3, -3, -3]"
    )


def test_lists_with_zeros():
    assert list_plus_list.get_lists_sum([0, 0, 0], [0, 0, 0]) == 0, (
        "Function 'get_lists_sum' should return 0 "
        "when ls1 is equal to [0, 0, 0] and ls2 is equal to [0, 0, 0]"
    )


def test_long_lists_with_big_numbers():
    assert (
        list_plus_list.get_lists_sum(
            [88, 93, -1, 25, -88, 99, 47, -44, 39, -94],
            [-47, -92, -46, 48, 59, -29, -87, -26, -21, 84],
        )
        == 7
    ), (
        "Function 'get_lists_sum' should return 7 "
        "when ls1 is equal to [88, 93, -1, 25, -88, 99, 47, -44, 39, -94] "
        "and ls2 is equal to [-47, -92, -46, 48, 59, -29, -87, -26, -21, 84]"
    )
