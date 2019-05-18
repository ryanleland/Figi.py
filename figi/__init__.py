__version__ = "0.0.1"
__doc__ = "Simple OpenFIGI client for Python 3."

import os
import json
import requests


class Figi():
    BASE_URL: str = "https://api.openfigi.com/v2"

    def __init__(self, api_key: str = None):
        if not api_key:
            api_key = os.environ.get("FIGI_API_KEY")

        self.api_key = api_key

    def search(self, query, **kwargs):
        data = {
            "query": query
        }
        data.update(kwargs)

        return self._request("search", data).get("data")

    def _request(self, endpoint: str, data: dict):
        url = f"{self.BASE_URL}/{endpoint}"
        data = json.dumps(data)
        response = requests.post(url, data=data, headers={
            "Content-Type": "application/json",
            "X-OPENFIGI-APIKEY": self.api_key
        })

        if response.status_code != 200:
            raise Exception(f"OpenFIGI Connection Error: {response.content}")

        return response.json()


class FigiException(Exception):
    pass