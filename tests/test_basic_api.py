"""Test the basic Api."""

# standard
import pytest
import json
import logging
from unittest.mock import patch, Mock

# local
from basic_api import BasicApi

logger = logging.getLogger(__name__)

# Sample test data
API_KEY = "test_api_key"
BASE_URL = "https://api.random.org/json-rpc/4/invoke"
VERSION = 4
VERSION_STR = "4.0"
NUM = 5
MIN = 1
MAX = 10
DECIMAL_PLACES = 2
LENGTH = [5, 5]
SEQUENCE_MIN = [1, 1]
SEQUENCE_MAX = [10, 10]
SEQUENCE_REPLACEMENT = [True, False]
REPLACEMENT = True
BASE = 10
MEAN = 0
STANDARD_DEVIATION = 1
SIGNIFICANT_DIGITS = 5
SIZE = 128
CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
UUID_NUM = 2


@pytest.fixture
def basic_api():
    """Fixture to create an instance of BasicApi."""
    return BasicApi(api_key=API_KEY)


def mock_post_response(mocked_post, response_data):
    """Mock the requests.post response."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = response_data
    mocked_post.return_value = mock_response


def test_generate_integers(basic_api):
    """Test generate_integers method to ensure it returns a valid list of integers."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "random": {"data": [1, 2]},
                        "requestsLeft": 1000,
                        "bitsLeft": 1000,
                    }
                }
            ),
        )
        result = basic_api.generate_integers(num=NUM, minimum=MIN, maximum=MAX)
        assert isinstance(result, list)
        assert len(result) == 2
        assert result == [1, 2]


def test_generate_integer_sequences(basic_api):
    """Test method to ensure it returns valid integer sequences."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "random": {"data": [[1, 2], [3, 4]]},
                        "requestsLeft": 1000,
                        "bitsLeft": 1000,
                    }
                }
            ),
        )
        result = basic_api.generate_integer_sequences(
            num=NUM, length=LENGTH, minimum=SEQUENCE_MIN, maximum=SEQUENCE_MAX
        )
        assert isinstance(result, list)
        assert len(result) == 2
        assert result == [[1, 2], [3, 4]]


def test_generate_decimal_fractions(basic_api):
    """Test method to ensure it returns a valid list of decimal numbers."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "random": {"data": [0.12, 0.34]},
                        "requestsLeft": 1000,
                        "bitsLeft": 1000,
                    }
                }
            ),
        )
        result = basic_api.generate_decimal_fractions(
            num=NUM, decimal_places=DECIMAL_PLACES
        )
        assert isinstance(result, list)
        assert result == [0.12, 0.34]


def test_generate_gaussians(basic_api):
    """Test method to ensure it returns Gaussian-distributed numbers."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "random": {"data": [0.123, -0.456]},
                        "requestsLeft": 1000,
                        "bitsLeft": 1000,
                    }
                }
            ),
        )
        result = basic_api.generate_gaussians(
            num=NUM,
            mean=MEAN,
            standard_deviation=STANDARD_DEVIATION,
            significant_digits=SIGNIFICANT_DIGITS,
        )
        assert isinstance(result, list)
        assert result == [0.123, -0.456]


def test_generate_strings(basic_api):
    """Test method to ensure it returns a valid list of random strings."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "random": {"data": ["abcde", "fghij"]},
                        "requestsLeft": 1000,
                        "bitsLeft": 1000,
                    }
                }
            ),
        )
        result = basic_api.generate_strings(num=NUM, length=5, characters=CHARACTERS)
        assert isinstance(result, list)
        assert result == ["abcde", "fghij"]


def test_generate_uuids(basic_api):
    """Test generate_uuids method to ensure it returns a valid list of UUIDs."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "random": {
                            "data": [
                                "123e4567-e89b-12d3-a456-426614174000",
                                "123e4567-e89b-12d3-a456-426614174001",
                            ]
                        },
                        "requestsLeft": 1000,
                        "bitsLeft": 1000,
                    }
                }
            ),
        )
        result = basic_api.generate_uuids(num=UUID_NUM)
        assert isinstance(result, list)
        assert len(result) == 2


def test_generate_blobs(basic_api):
    """Test method to ensure it returns a valid list of random blobs."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "random": {"data": ["blob_data_1", "blob_data_2"]},
                        "requestsLeft": 1000,
                        "bitsLeft": 1000,
                    }
                }
            ),
        )
        result = basic_api.generate_blobs(num=NUM, size=SIZE)
        assert isinstance(result, list)
        assert len(result) == 2


def test_get_usage(basic_api):
    """Test method to ensure it returns a dictionary of API usage statistics."""
    with patch("requests.post") as mocked_post:
        mock_post_response(
            mocked_post,
            json.dumps(
                {
                    "result": {
                        "bitsLeft": 1000,
                        "requestsLeft": 100,
                        "totalBits": 2000,
                        "totalRequests": 200,
                    }
                }
            ),
        )
        result = basic_api.get_usage()
        assert isinstance(result, dict)
        assert result["bits_left"] == 1000
        assert result["requests_left"] == 100
        assert result["total_bits"] == 2000
        assert result["total_requests"] == 200
