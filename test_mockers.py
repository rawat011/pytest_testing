import pytest
from robin_utils import get_api_resp

def test_mock_api_resp(mocker):
    mock_resp = mocker.Mock()
    mock_resp.status = 200
    mock_resp.json.return_value = {"status": "Ready", "id": 123}
    mocker.patch("robin_utils.requests.get", return_value=mock_resp)

    resp = get_api_resp("vm")
    assert resp == "Ready"