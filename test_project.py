from project import hello

# This test function checks if the hello() function works correctly
def test_hello_returns_correct_string():
    # 'assert' is the magic word.
    # It checks if the condition that follows is True.
    # If it's True, the test passes.
    # If it's False, the test fails and prints an error.
    assert hello() == "Hello, world!"

def test_hello_is_not_goodbye():
    # This checks that the student *changed* the default code.
    assert hello() != "Goodbye, world!"
