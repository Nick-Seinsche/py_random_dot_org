"""Module for interacting with the Random.org Basic API to generate random data."""

import requests
import json
import logging

logger = logging.getLogger(__name__)


class BasicApi:
    """Basic Api Wrapper for the Random.org API."""

    def __init__(
        self,
        api_key: str,
        version: int = 4,
        version_str: str = "4.0",
        warn_below_quota_requests: int = 0,
        warn_below_quota_bits: int = 0,
    ) -> None:
        """
        Initialize the class.

        Args:
            api_key (str): The API key for authentication.
            version (int): The version of the API to use. Defaults to 4.
            version_str (str): The version string of the API. Defaults to "4.0".
            warn_below_quota_requests (int): The number of requests below which to
                issue a warning. Defaults to 0.
            warn_below_quota_bits (int): The number of bits below which to issue a
                warning. Defaults to 0.
        """
        self.url = f"https://api.random.org/json-rpc/{str(version)}/invoke"
        self.api_key = api_key
        self.version_str = version_str
        self.warn_below_quota_requests = warn_below_quota_requests
        self.warn_below_quota_bits = warn_below_quota_bits

    def generate_integers(
        self,
        num: int,
        minimum: int,
        maximum: int,
        replacement: bool = True,
        base: int = 10,
        pregenerateRandomiztion: dict | None = None,
        id: int = 1,
    ) -> list[int | str]:
        """
        Generate true random integers within a user-defined range.

        Args:
            num (int): The number of integers to generate.
            minimum (int): The minimum value of the integers.
            maximum (int): The maximum value of the integers.
            replacement (bool): Whether to allow replacement of values.
                Defaults to True.
            base (int): The base for encoding the integers. Defaults to 10.
            pregenerateRandomiztion (dict | None): Optional parameter for
                pre-generation randomization. Defaults to None.
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            list[int | str]: The generated integers.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "generateIntegers",
            "params": {
                "apiKey": self.api_key,
                "n": num,
                "min": minimum,
                "max": maximum,
                "replacement": replacement,
                "base": base,
            },
            "id": id,
        }
        return self._request(
            method="generate_integers",
            request_payload=payload,
            data_retrieve_func=lambda x: x["random"]["data"],
        )

    def generate_integer_sequences(
        self,
        num: int,
        length: list[int],
        minimum: list[int],
        maximum: list[int],
        replacement: list[bool] = None,
        base: list[int] = 10,
        id: int = 1,
    ) -> list[list[int]]:
        """
        Generate integer sequences.

        Args:
            num (int): The number of sequences to generate.
            length (list[int]): The lengths of the sequences.
            minimum (list[int]): The minimum values for each sequence.
            maximum (list[int]): The maximum values for each sequence.
            replacement (list[bool]): Whether to allow replacement of values in
                each sequence. Defaults to None.
            base (list[int]): The base for encoding the integers in each sequence.
                Defaults to 10.
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            The generated sequences.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "generateIntegerSequences",
            "params": {
                "apiKey": self.api_key,
                "n": num,
                "length": length,
                "min": minimum,
                "max": maximum,
                "replacement": replacement,
                "base": list[int],
            },
            "id": id,
        }
        return self._request(
            method="generate_integer_sequences",
            request_payload=payload,
            data_retrieve_func=lambda x: x["random"]["data"],
        )

    def generate_decimal_fractions(
        self,
        num: int,
        decimal_places: int,
        replacement=True,
        id: int = 1,
    ) -> list[float]:
        """
        Generate decimal fractions.

        Args:
            num (int): The number of decimal fractions to generate.
            decimal_places (int): The number of decimal places for each fraction.
            replacement (bool): Whether to allow replacement of values.
                Defaults to True.
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            The generated decimal fractions.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "generateDecimalFractions",
            "params": {
                "apiKey": self.api_key,
                "n": num,
                "decimalPlaces": decimal_places,
                "replacement": replacement,
            },
            "id": id,
        }
        return self._request(
            method="generate_decimal_fractions",
            request_payload=payload,
            data_retrieve_func=lambda x: x["random"]["data"],
        )

    def generate_gaussians(
        self,
        num: int,
        mean: float,
        standard_deviation: float,
        significant_digits: int,
        id: int = 1,
    ) -> list[float]:
        """
        Generate Gaussian-distributed numbers.

        Args:
            num (int): The number of Gaussian numbers to generate.
            mean (float): The mean of the Gaussian distribution.
            standard_deviation (float): The standard deviation of the
                Gaussian distribution.
            significant_digits (int): The number of significant digits for the output.
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            The generated Gaussian-distributed numbers.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "generateGaussians",
            "params": {
                "apiKey": self.api_key,
                "n": num,
                "mean": mean,
                "standardDeviation": standard_deviation,
                "significantDigits": significant_digits,
            },
            "id": id,
        }
        return self._request(
            method="generate_gaussians",
            request_payload=payload,
            data_retrieve_func=lambda x: x["random"]["data"],
        )

    def generate_strings(
        self, num: int, length: int, characters: str, replacement=True, id=1
    ) -> list[str]:
        """
        Generate random strings.

        Args:
            num (int): The number of strings to generate.
            length (int): The length of each string.
            characters (str): The characters to use for generating the strings.
            replacement (bool): Whether to allow replacement of characters.
                Defaults to True.
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            The generated strings.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "generateStrings",
            "params": {
                "apiKey": self.api_key,
                "n": num,
                "length": length,
                "characters": characters,
                "replacement": replacement,
            },
            "id": id,
        }

        return self._request(
            method="generate_strings",
            request_payload=payload,
            data_retrieve_func=lambda x: x["random"]["data"],
        )

    def generate_uuids(self, num: int, id=1) -> list[str]:
        """
        Generate UUIDs.

        Args:
            num (int): The number of UUIDs to generate.
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            The generated UUIDs.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "generateUUIDs",
            "params": {"apiKey": self.api_key, "n": num},
            "id": id,
        }
        return self._request(
            method="generate_uuids",
            request_payload=payload,
            data_retrieve_func=lambda x: x["random"]["data"],
        )

    def generate_blobs(self, num: int, size: int, id=1) -> list[str]:
        """
        Generate random blobs of data.

        Args:
            num (int): The number of blobs to generate.
            size (int): The size of each blob in bytes.
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            The generated blobs of data.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "generateBlobs",
            "params": {
                "apiKey": self.api_key,
                "n": num,
                "size": size,
            },
            "id": id,
        }
        return self._request(
            method="generate_blobs",
            request_payload=payload,
            data_retrieve_func=lambda x: x["random"]["data"],
        )

    def get_usage(self, id: int = 1) -> tuple:
        """
        Get the API usage statistics.

        Args:
            id (int): The identifier for the request. Defaults to 1.

        Returns:
            dict: A dictionary containing usage statistics, including bits left,
            requests left, total bits, and total requests.
        """
        payload = {
            "jsonrpc": self.version_str,
            "method": "getUsage",
            "params": {
                "apiKey": self.api_key,
            },
            "id": id,
        }
        return self._request(
            method="get_usage",
            request_payload=payload,
            data_retrieve_func=lambda x: {
                "bits_left": x["bitsLeft"],
                "requests_left": x["requestsLeft"],
                "total_bits": x["totalBits"],
                "total_requests": x["totalRequests"],
            },
        )

    def _request(self, method, request_payload, data_retrieve_func=None):
        """Pipeline for one API request."""
        response = self._robust_http_request(request_payload, "generate_integers")

        if response is not None:
            self._is_response_successful(response.status_code, "generate_integers")

        response_data, requests_left, bits_left = self._extract_result(
            response, data_retrieve_func, "generate_integers"
        )

        self._is_low_quota(requests_left, bits_left)
        self._log_sucess("generate_integers")

        return response_data

    def _robust_http_request(self, payload: dict, method=""):
        """Robust request."""
        try:
            response = requests.post(self.url, json=payload)
        except ConnectionError:
            logger.error(
                f"A ConnectionError occured during basicApi.{method}()",
                exc_info=True,
            )
            return
        return response

    def _extract_result(self, response, data_retrieve_func=None, method: str = ""):
        """Extract results from returned payload."""

        def default_func(x):
            return x

        if data_retrieve_func is None:
            data_retrieve_func = default_func

        try:
            response_result = json.loads(response.content)["result"]
            response_data = data_retrieve_func(response_result)
            requests_left = response_result["requestsLeft"]
            bits_left = response_result["bitsLeft"]
        except Exception:
            logger.error(f"Could not decode the http response of basicApi.{method}()")
            return
        return response_data, requests_left, bits_left

    def _is_response_successful(self, status_code, method=""):
        """Check http response code for success."""
        if not (200 <= status_code <= 299):
            logger.warning(
                "Response Code indicates non succesful request for "
                f"basicApi.{method}()"
            )
            return True
        return False

    def _is_low_quota(self, requests_left, bits_left):
        """Check if quota is low."""
        if (
            self.warn_below_quota_requests
            and requests_left < self.warn_below_quota_requests
        ):
            logger.warning("Low Request-Quota for API.")
            return True

        if self.warn_below_quota_bits and bits_left < self.warn_below_quota_bits:
            logging.warning("Low Bit-Quota for API.")
            return True
        return False

    def _log_sucess(self, method: str = ""):
        logger.debug(f"Sucessfully retrieved basicApi.{method}()")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        filename="../logs/log.log",
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    import os

    api = BasicApi(api_key=os.getenv("API_KEY"))
    resp = api.generate_integers(2, 1, 100)
    print(resp)
