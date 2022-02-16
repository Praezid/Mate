from tasks.extra_tasks.simple_math_checker import simple_math_checker


def test_true_false_false_when_number_is_3():
    assert simple_math_checker.check_number(3) == [True, False, False], (
        "Function 'check_number' should return [True, False, False] "
        "when number is 3"
    )


def test_true_true_true_when_number_is_10():
    assert simple_math_checker.check_number(10) == [True, True, True], (
        "Function 'check_number' should return [True, True, True] "
        "when number is 10"
    )


def test_false_true_true_when_number_is_0():
    assert simple_math_checker.check_number(0) == [False, True, True], (
        "Function 'check_number' should return [False, True, True] "
        "when number is 0"
    )


def test_false_false_false_when_number_is_odd_and_negative():
    assert simple_math_checker.check_number(-1) == [False, False, False], (
        "Function 'check_number' should return [False, False, False] "
        "when number is -1"
    )


def test_false_true_false_when_number_is_even_and_negative():
    assert simple_math_checker.check_number(-2) == [False, True, False], (
        "Function 'check_number' should return [False, True, False] "
        "when number is -2"
    )


def test_false_true_true_when_number_is_negative_and_divisible_by_10():
    assert simple_math_checker.check_number(-100) == [False, True, True], (
        "Function 'check_number' should return [False, True, True] "
        "when number is -100"
    )


def test_true_true_false_when_number_is_44():
    assert simple_math_checker.check_number(44) == [True, True, False], (
        "Function 'check_number' should return [True, True, False] "
        "when number is 44"
    )
