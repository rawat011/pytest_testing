# Example Usage:
from my_request import get_client

def test_user_repos_api():
    client = get_client()
    data = client.get_resource("repos/rawat011/nasa-potd/contents/main.py")
    print(data)
#
# # test_user_api()
#
# def test_user_emails_api():
#     client = get_client()
#     data = client.get_resource("user")
#     print(data)

# def test_gists_api():
#     client = get_client()
#     data = client.get_resource("gists")
#     print(data)

# test_user_api()