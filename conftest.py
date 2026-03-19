import pytest
@pytest.fixture(scope='package')
def api_client():
    # Setup: Initialize the client
    print("\nConnecting to Robin.io API...")
    client = {"auth": "success", "version": "5.3"}

    yield client  # This is where the test happens

    # Teardown: Clean up resources
    print("\nClosing API connection...")

@pytest.fixture(scope='function')
def loggin():
    print("logging in")
    yield
    print("logging out")


def pytest_addoption(parser):
    """Register custom command-line arguments."""
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against: qa, dev, or prod"
    )

@pytest.fixture(scope="session")
def env_config(request):
    """Fixture that reads the command-line argument."""
    selected_env = request.config.getoption("--env")

    # Mapping environments to their Robin.io cluster URLs
    configs = {
        "dev": {"url": "https://dev-robin.local", "timeout": 30},
        "qa": {"url": "https://qa-robin.local", "timeout": 60},
        "prod": {"url": "https://api.robin.io", "timeout": 120}
    }

    return configs.get(selected_env, configs["qa"])