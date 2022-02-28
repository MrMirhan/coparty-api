import requests

print(requests.get("http://45.131.3.98", params={"a": "b"}, json={"x": "y"}).content)