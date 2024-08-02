import pytest



@pytest.fixture(scope="function")
def function_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def class_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


# @pytest.fixture(autouse=True)
# def always_used_fixture():
#     print(f"\n Hello, I'm fixture with autouse and funcction scope used always!")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL to test, default is https://ya.ru"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(params=[
    "https://dog.ceo/api/breeds/list/all",
    "https://dog.ceo/api/breeds/list/random"
], ids=["All Breeds", "Random Breed"])
def param_url(request):
    return request.param