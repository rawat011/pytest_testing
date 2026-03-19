import requests

def get_api_resp(service):
    # api = f"/api/storage/disk/{service}"

    url = f"https://api.robin.io/v1/apps/{service}"
    resp = requests.get(url)

    return resp.json()['status']
