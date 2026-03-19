import pytest
@pytest.fixture(scope='package')
def api_client():
    # Setup: Initialize the client
    print("\nConnecting to Robin.io API...")
    client = {"auth": "success", "version": "5.3"}

    yield client  # This is where the test happens

    # Teardown: Clean up resources
    print("\nClosing API connection...")
