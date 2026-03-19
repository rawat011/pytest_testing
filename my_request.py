import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

import os
from dotenv import load_dotenv

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        # Using a Session persists headers and reuses TCP connections
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        })

    def get_resource(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            # Always set a timeout to prevent the script from hanging
            response = self.session.get(url, params=params, timeout=10)

            # Raises an HTTPError if the status is 4xx or 5xx
            response.raise_for_status()

            return response.json()

        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except ConnectionError:
            print("Connection error: Check your internet or the server status.")
        except Timeout:
            print("The request timed out.")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
        return None

_client_instance = None

def get_client():
    global _client_instance
    if _client_instance is None:
        load_dotenv()
        TOKEN = os.getenv("API_TOKEN")
        _client_instance = APIClient("https://api.github.com", TOKEN)
    return _client_instance