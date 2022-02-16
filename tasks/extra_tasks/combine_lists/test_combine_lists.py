from tasks.extra_tasks.combine_lists.combine_lists import combine_lists


def test_empty_list_when_given_lists_are_empty():
    assert combine_lists([], []) == [], (
        "Function 'combine_lists' should return an empty list "
        "when ls1 and ls2 are empty"
    )


def test_one_item_lists():
    assert combine_lists([2], [2]) == [4], (
        "Function 'combine_lists' should return [4] "
        "when ls1 is equal to [2] and ls2 is equal to [2]"
    )


def test_lists_of_zeros():
    assert combine_lists([0, 0, 0], [0, 0, 0]) == [0, 0, 0], (
        "Function 'combine_lists' should return [0, 0, 0] "
        "when ls1 is equal to [0, 0, 0] and ls2 is equal to [0, 0, 0]"
    )


def test_short_lists():
    assert combine_lists([12, 123], [33, 82]) == [45, 205], (
        "Function 'combine_lists' should return [45, 205] "
        "when ls1 is equal to [12, 123] and ls2 is equal to [33, 82]"
    )


def test_lists_with_negative_numbers():
    assert combine_lists([112, -123], [-12, 83]) == [100, -40], (
        "Function 'combine_lists' should return [100, -40] "
        "when ls1 is equal to [112, -123] and ls2 is equal to [-12, 83]"
    )


def test_long_lists():
    assert (
        combine_lists(
            [24, 47, 11, 64, 67, 41, 81, 19, 13, 7],
            [48, 14, 9, 38, 51, 25, 2, 99, 56, 29],
        )
        == [72, 61, 20, 102, 118, 66, 83, 118, 69, 36]
    ), (
        "Function 'combine_lists' should return [72, 61, 20, 102, 118, 66, 83, 118, 69, 36] "
        "when ls1 is equal to [24, 47, 11, 64, 67, 41, 81, 19, 13, 7] "
        "and ls2 is equal to [48, 14, 9, 38, 51, 25, 2, 99, 56, 29]"
    )
