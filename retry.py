from tenacity import retry, stop_after_attempt, wait_fixed

def get_status():
    for i in range(5):
        if i < 3:
            yield "NOTOK"
        else:
            yield "OK"

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def check_status(status):
    s = next(status)
    print(s)
    if s != "OK":
        raise Exception("Status is not OK")
    return True

def test_check_status():
    status = get_status()
    assert check_status(status)