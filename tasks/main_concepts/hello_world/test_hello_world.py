from io import StringIO
import sys


def test_hello_world():
    prev_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    from tasks.main_concepts.hello_world import hello_world

    assert captured_output.getvalue() == "Hello, world!\n"

    sys.stdout = prev_stdout
