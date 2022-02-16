from tasks.main_concepts.uncomment_code import uncomment_code


def test_name_should_be_uncommented():
    assert (
        hasattr(uncomment_code, "name") is True
    ), "Variable 'name' should be uncommented"
    name = uncomment_code.name
    assert name == "Oleg", "Variable 'name' should not be modified"


def test_age_should_be_uncommented():
    assert (
        hasattr(uncomment_code, "age") is True
    ), "Variable 'age' should be uncommented"
    age = uncomment_code.age
    assert age == 22, "Variable 'age' should not be modified"
