import pytest
import time

pytestmark = pytest.mark.reg

@pytest.mark.smoke
def test_login_api():
    time.sleep(5)
    assert True

@pytest.mark.storage
@pytest.mark.regression
def test_volume_provisioning():
    # This test belongs to TWO groups
    time.sleep(3)
    assert True

@pytest.mark.networking
def test_pod_connectivity():
    time.sleep(4)
    assert True