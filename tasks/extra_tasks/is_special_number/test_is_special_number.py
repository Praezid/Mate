from tasks.extra_tasks.is_special_number import is_special_number


def test_special_when_number_is_single_digit_and_less_than_5():
    assert (
        is_special_number.is_special_number(3) == "Special!!"
    ), "Function 'is_special_number' should return 'Special!!' when number is equal to 3"
    assert (
        is_special_number.is_special_number(5) == "Special!!"
    ), "Function 'is_special_number' should return 'Special!!' when number is equal to 5"
    assert (
        is_special_number.is_special_number(0) == "Special!!"
    ), "Function 'is_special_number' should return 'Special!!' when number is equal to 0"


def test_not_when_number_is_single_digit_and_grater_than_5():
    assert (
        is_special_number.is_special_number(6) == "NOT!!"
    ), "Function 'is_special_number' should return 'NOT!!' when number is equal to 6"
    assert (
        is_special_number.is_special_number(9) == "NOT!!"
    ), "Function 'is_special_number' should return 'NOT!!' when number is equal to 9"
    assert (
        is_special_number.is_special_number(8) == "NOT!!"
    ), "Function 'is_special_number' should return 'NOT!!' when number is equal to 8"


def test_not_when_number_contains_digits_that_grater_than_5():
    assert (
        is_special_number.is_special_number(1236) == "NOT!!"
    ), "Function 'is_special_number' should return 'NOT!!' when number is equal to 1236"
    assert (
        is_special_number.is_special_number(1111381123) == "NOT!!"
    ), "Function 'is_special_number' should return 'NOT!!' when number is equal to 1111381123"
    assert (
        is_special_number.is_special_number(55555565) == "NOT!!"
    ), "Function 'is_special_number' should return 'NOT!!' when number is equal to 55555565"
    assert (
        is_special_number.is_special_number(700) == "NOT!!"
    ), "Function 'is_special_number' should return 'NOT!!' when number is equal to 700"


def test_special_when_number_does_not_contain_digits_that_grater_than_5():
    assert (
        is_special_number.is_special_number(122341) == "Special!!"
    ), "Function 'is_special_number' should return 'Special!!' when number is equal to 122341"
    assert (
        is_special_number.is_special_number(4321) == "Special!!"
    ), "Function 'is_special_number' should return 'Special!!' when number is equal to 4321"
    assert (
        is_special_number.is_special_number(55555) == "Special!!"
    ), "Function 'is_special_number' should return 'Special!!' when number is equal to 55555"
