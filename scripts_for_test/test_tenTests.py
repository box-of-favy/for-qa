import pytest

l = []
print("Type: ", type(l))
l.append(1)
l.append('1')
l.extend([2,3,4])
print("l -> ", l)

def test_one(function_fixture, class_fixture, module_fixture, session_fixture):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert 10 in numbers, "Число 10 должно быть в списке"

# Создание тестовых файлов
def test_two():
    print(" >>>I'm test one!")

@pytest.fixture(scope="session")
def session_data():
    """Session level fixture for data shared across tests."""
    return {"key": "value"}

@pytest.fixture(scope="module")
def module_list():
    """Module level fixture to provide a list."""
    return [1, 2, 3, 4, 5, 6, 7, 8]

@pytest.fixture(scope="function")
def function_dict():
    """Function level fixture to provide a dictionary."""
    return {"one": 1, "two": 2}

def test_list_length(module_list):
    """Test that the length of the list is 8."""
    assert len(module_list) == 8

def test_add_strings():
    """Test that concatenating two strings works correctly."""
    assert "Hello" + " World" == "Hello World"

def test_dict_values(function_dict):
    """Test that the values in the dictionary are as expected."""
    assert function_dict["one"] == 1
    assert function_dict["two"] == 2

def test_set_operations():
    """Test basic operations with sets."""
    sample_set = {1, 2, 3}
    sample_set.add(4)
    assert 4 in sample_set

def test_tuple_operations():
    """Test basic operations with tuples."""
    sample_tuple = (1, 2, 3)
    assert sample_tuple[0] == 1

def test_multiplication():
    """Test multiplication of numbers."""
    assert 2 * 3 == 6

def test_subtraction():
    """Test subtraction of numbers."""
    assert 5 - 3 == 2

def test_list_append(module_list):
    """Test appending to a list."""
    module_list.append(9)
    assert module_list[-1] == 9

def test_dict_update(function_dict):
    """Test updating a dictionary."""
    function_dict["three"] = 3
    assert function_dict["three"] == 3

def test_set_union():
    """Test union of sets."""
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    assert set1.union(set2) == {1, 2, 3, 4, 5}

@pytest.fixture(scope="function", autouse=True)
def function_teardown():
    """Fixture to perform teardown after each function."""
    yield
    print("\nTeardown after test function")

@pytest.fixture(scope="module", autouse=True)
def module_teardown():
    """Fixture to perform teardown after each module."""
    yield
    print("\nTeardown after module")

@pytest.fixture(scope="session", autouse=True)
def session_teardown():
    """Fixture to perform teardown after the session."""
    yield
    print("\nTeardown after session")







# так можно, но не нужно, и с модулем не заработает
def testtwo():
    pass
# Создание тестовых классов
class TestClass:

    def test_one(self):
        pass

    def test_two(self):
        pass

