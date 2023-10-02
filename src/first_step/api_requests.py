import requests
import os


class SplunkDataFetcher:
    def __init__(self):
        self.payload = {
            "search": "search `CILMSTransactions` cf_app_name=smartsearch-api | table _time, msg, cf_org_name, cf_app_name, _raw"
        }
        self.splunk_url = os.getenv("FLASK_SPLUNK_URL")
        self._session = requests.Session()

    @property
    def session(self):
        return self._session

    def fetch_data_from_splunk(self):
        """
        Fetches data from Splunk and handles potential errors.

        Sends an HTTP POST request to the Splunk API with the configured payload
        and URL. Handles various types of exceptions that may occur during the
        request, printing corresponding error messages.

        Returns:
            dict or None: The response JSON as a dictionary if successful, or None
            in case of an error.

        """
        try:
            response = self.session.post(self.splunk_url, json=self.payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    splunk_data_fetcher = SplunkDataFetcher()
    print(splunk_data_fetcher.fetch_data_from_splunk())
    print(splunk_data_fetcher.session)
