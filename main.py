import requests
import datetime
import pytz
from http import HTTPStatus

# Custom status code → meaning map (based on your image)
status_meanings = {
    200: "Request succeeded",
    201: "Resource created (usually POST)",
    204: "Successful, but no data in response",
    301: "Resource permanently moved",
    302: "Temporary redirect",
    400: "Invalid request syntax",
    401: "Authentication required",
    403: "Access denied",
    404: "URL doesn’t exist",
    408: "Server timed out waiting for request",
    429: "Rate limit hit",
    500: "Server had an unexpected issue",
    502: "Invalid response from upstream server",
    503: "Server is down or overloaded",
    504: "Upstream server didn’t respond in time"
}

def check_api(request):
    url = "https://allgen.ghbapp.com/mobile_config/th/contact.json"
    bangkok_tz = pytz.timezone("Asia/Bangkok")
    now = datetime.datetime.now(bangkok_tz).strftime("%Y-%m-%d %H:%M:%S")

    try:
        response = requests.get(url, timeout=5)
        code = response.status_code
        phrase = HTTPStatus(code).phrase if code in HTTPStatus._value2member_map_ else "Unknown"
        meaning = status_meanings.get(code, "No explanation available")

        if code == 200:
            status = f"✅ allgen.ghbapp.com API OK: {code} ({phrase}) - {meaning}"
        else:
            status = f"❌ allgen.ghbapp.com API ERROR: {code} ({phrase}) - {meaning}"

    except requests.exceptions.RequestException as e:
        status = f"❌ allgen.ghbapp.com API ERROR: Exception - {str(e)}"

    return f"{now} {status}"
'''
if __name__ == "__main__":
    print(check_api(None))
'''