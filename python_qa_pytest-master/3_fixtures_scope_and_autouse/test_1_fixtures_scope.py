def test_one(function_fixture, class_fixture, module_fixture, session_fixture):
    print("I test_one NOT in test class 1!")


def test_two(function_fixture, class_fixture, module_fixture, session_fixture):
    print("I test_two NOT in test class 2!")


class TestClass:
    def __init__(self, function_fixture, class_fixture, module_fixture, session_fixture):
        self.function_fixture = function_fixture
        self.class_fixture = class_fixture
        self.module_fixture = module_fixture
        self.session_fixture = session_fixture
    def test_one(self):
        print("Im test_one in TestClass test class!")

    def test_two(self):
        print("Im test_two in TestClass test class!")

    def test_three(self):
        print("Im test_three in TestClass test class!")

class TestClass2(TestClass):
    def test_four(self):
        print("Im test_four in TestClass test class!")