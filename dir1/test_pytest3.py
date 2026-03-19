import pytest

class TestFixures2():
    @pytest.fixture(scope='package')
    def api_client(self):
        # Setup: Initialize the client
        print("\nConnecting to Robin.io API...")
        client = {"auth": "success", "version": "5.3"}

        yield client  # This is where the test happens

        # Teardown: Clean up resources
        print("\nClosing API connection...")

    def test_conenction(self, api_client):
        assert api_client['auth'] == "success"

    def test_api_version(self, api_client):
        assert api_client['version'] == "5.3"

class TestFixures1():
    # @pytest.fixture(scope='function')
    # def api_client(self):
    #     # Setup: Initialize the client
    #     print("\nConnecting to Robin.io API...")
    #     client = {"auth": "success", "version": "5.3"}
    #
    #     yield client  # This is where the test happens
    #
    #     # Teardown: Clean up resources
    #     print("\nClosing API connection...")

    def test_conenction(self, api_client):
        assert api_client['auth'] == "success"

    def test_api_version(self, api_client):
        assert api_client['version'] == "5.3"

# def test_volume_size_conversion():
#     gb_size = 10
#     mb_size = gb_size * 1024
#     assert mb_size == 10240
#
# def test_string_format():
#     node_name = "robin-node-01"
#     assert node_name.startswith("robin")