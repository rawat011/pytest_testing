import pytest

@pytest.mark.parametrize("x", [1,2,3,4])
def test_x(x):
    assert x < 5