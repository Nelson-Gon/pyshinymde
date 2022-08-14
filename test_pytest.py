import pytest 
from our_project.hello_world import HelloWorld

@pytest.fixture 
def test_obj():
    return HelloWorld(hello_text="Hello World")
    
# Weird that we need to pass fixtures as arguments to other functions 
def test_init(test_obj):
    assert isinstance(test_obj, HelloWorld)

def test_hello_text_print(test_obj):
    assert test_obj.print_text() == "Hello World"
    with pytest.raises(AssertionError) as err:
        HelloWorld(hello_text=420.42)
        assert str(err.exception) == "hello_text must be a string not float"

