import pytest


# СНАЧАЛА ПРО SCOPE!

@pytest.fixture(autouse=True)
def function_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")
    def fin():
        print(f"\n Finalize from {request.scope} fixture!")
    request.addfinalizer(fin)

@pytest.fixture(scope="class", autouse=True)
def class_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")
    def fin():
        print(f"\n Finalize from {request.scope} fixture!")
    request.addfinalizer(fin)

@pytest.fixture(scope="module", autouse=True)
def module_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")
    def fin():
        print(f"\n Finalize from {request.scope} fixture!")
    request.addfinalizer(fin)

@pytest.fixture(scope="session", autouse=True)
def session_fixture(request):
    print(f"\n Hello from {request.scope.upper()} fixture!")
    def fin():
        print(f"\n Finalize from {request.scope.upper()} fixture!")
    request.addfinalizer(fin)


def test_one():
    print('abc')
    pass


def test_two():
    print('dfg')
    pass


class TestClass:

    def test_one(self):
        print(' first class autouse')
        pass

    def test_two(self):
        print(' second class autouse')
        pass
