from tasks.extra_tasks.jumping_numbers import jumping_numbers


def test_jumping_when_number_is_one_digit():
    assert (
            jumping_numbers.is_jumping(9) == "JUMPING"
    ), "Function 'is_jumping' should return 'JUMPING' when number is 9"

    assert (
            jumping_numbers.is_jumping(1) == "JUMPING"
    ), "Function 'is_jumping' should return 'JUMPING' when number is 1"

    assert (
            jumping_numbers.is_jumping(0) == "JUMPING"
    ), "Function 'is_jumping' should return 'JUMPING' when number is 0"


def test_not_jumping_when_number_is_79():
    assert jumping_numbers.is_jumping(79) == "NOT JUMPING", (
        "Function 'is_jumping' should return 'NOT JUMPING' "
        "when number is 79"
    )


def test_jumping_when_number_is_23454():
    assert (
            jumping_numbers.is_jumping(23454) == "JUMPING"
    ), "Function 'is_jumping' should return 'JUMPING' when number is 23454"


def test_not_jumping_when_number_is_97():
    assert jumping_numbers.is_jumping(97) == "NOT JUMPING", (
        "Function 'is_jumping' should return 'NOT JUMPING' "
        "when number is 97"
    )


def test_not_jumping_when_number_is_90():
    assert jumping_numbers.is_jumping(90) == "NOT JUMPING", (
        "Function 'is_jumping' should return 'NOT JUMPING' "
        "when number is 90"
    )


def test_not_jumping_when_number_is_12543():
    assert jumping_numbers.is_jumping(12543) == "NOT JUMPING", (
        "Function 'is_jumping' should return 'NOT JUMPING' "
        "when number is 12543"
    )


def test_not_jumping_when_number_is_123453():
    assert jumping_numbers.is_jumping(123453) == "NOT JUMPING", (
        "Function 'is_jumping' should return 'NOT JUMPING' "
        "when number is 123453"
    )


def test_jumping_when_number_is_789876567():
    assert jumping_numbers.is_jumping(789876567) == "JUMPING", (
        "Function 'is_jumping' should return 'JUMPING' "
        "when number is 789876567"
    )


def test_not_jumping_when_number_is_79876567():
    assert jumping_numbers.is_jumping(79876567) == "NOT JUMPING", (
        "Function 'is_jumping' should return 'NOT JUMPING' "
        "when number is 79876567"
    )


def test_not_jumping_when_number_consists_of_equal_digits():
    assert jumping_numbers.is_jumping(77) == "NOT JUMPING", (
        "Function 'is_jumping' should return 'NOT JUMPING' "
        "when number is 77"
    )
