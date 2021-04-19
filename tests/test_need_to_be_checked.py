from pathlib import Path
from unittest.mock import patch

import pytest

from timezone_checker.__main__ import transform, main, need_to_be_checked

HERE = Path(__file__).parent


@pytest.mark.parametrize(
    "content,expected",
    [
        [{}, False],
        [{"lon": 1.0, "lat": 0.5, "timezone": "Europe/Paris"}, True],
        [{"alt": 500, "lon": 1.0, "lat": 0.5, "timezone": "Europe/Paris"}, True],
        [{"key": {"lon": 1.0, "lat": 0.5, "timezone": "Europe/Paris"}}, True],
    ],
)
def test_need_to_be_checked(content, expected):
    assert need_to_be_checked(content, "lon", "lat", "timezone") is expected
