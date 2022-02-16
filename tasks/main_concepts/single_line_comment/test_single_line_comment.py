import re

from smarttekinternship.tasks.main_concepts.single_line_comment import single_line_comment


def test_single_line_comment():
    with open(single_line_comment.__file__, "r") as f:
        file_content = f.read()
        regex_bob = re.compile(r'#[ ]*name = "Oleg')
        assert regex_bob.search(
            file_content
        ), "Variable 'name' should be commented with single-line comment"
        regex_age = re.compile(r"#[ ]*age = 22")
        assert regex_age.search(
            file_content
        ), "Variable 'age' should be commented with single-line comment"
