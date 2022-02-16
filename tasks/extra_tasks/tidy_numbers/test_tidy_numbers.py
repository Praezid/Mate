from tasks.extra_tasks.tidy_numbers import tidy_numbers


def test_true_when_number_is_single_digit():
    assert (
        tidy_numbers.is_tidy(1) is True
    ), "Function 'is-tidy' should return True when number is 1"
    assert (
        tidy_numbers.is_tidy(3) is True
    ), "Function 'is-tidy' should return True when number is 3"
    assert (
        tidy_numbers.is_tidy(9) is True
    ), "Function 'is-tidy' should return True when number is 9"


def test_true_when_number_consists_of_non_decreasing_ordered_digits():
    assert (
        tidy_numbers.is_tidy(12) is True
    ), "Function 'is-tidy' should return True when number is 12"
    assert (
        tidy_numbers.is_tidy(12389) is True
    ), "Function 'is-tidy' should return True when number is 12389"
    assert (
        tidy_numbers.is_tidy(12334) is True
    ), "Function 'is-tidy' should return True when number is 12333"


def test_true_when_all_digits_in_the_number_are_same():
    assert (
        tidy_numbers.is_tidy(44) is True
    ), "Function 'is-tidy' should return True when number is 44"
    assert (
        tidy_numbers.is_tidy(55555) is True
    ), "Function 'is-tidy' should return True when number is 55555"


def test_false_when_number_consists_of_decreasing_ordered_digits():
    assert (
        tidy_numbers.is_tidy(43) is False
    ), "Function 'is-tidy' should return False when number is 43"
    assert (
        tidy_numbers.is_tidy(9871) is False
    ), "Function 'is-tidy' should return False when number is 9871"


def test_false_when_number_consists_of_unordered_digits():
    assert (
        tidy_numbers.is_tidy(12352) is False
    ), "Function 'is-tidy' should return False when number is 12352"
    assert (
        tidy_numbers.is_tidy(782266) is False
    ), "Function 'is-tidy' should return False when number is 782266"
