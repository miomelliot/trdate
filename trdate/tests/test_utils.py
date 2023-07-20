from ..code.utils import stringLines, splitLines

def test_stringLines():
    input_string = ["Hello", "world!"]
    expected_output = "Hello world!"
    assert stringLines(input_string) == expected_output

def test_splitLines():
    input_string = "Hello:world!"
    expected_output = ["Hello", "world!"]
    assert splitLines(input_string) == expected_output
