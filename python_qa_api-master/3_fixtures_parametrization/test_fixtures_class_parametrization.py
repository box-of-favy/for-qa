import pytest

@pytest.mark.parametrize("input,result", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, result):
   assert input + 1 == result

# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

# @pytest.mark.parametrize("test_input", [1, 2, 3])
# class TestClassParametrized:
#
#     # Все функци должны использовать аргумент
#     def test_one(self, test_input):
#         pass
#
#     def test_two(self, test_input):
#         pass