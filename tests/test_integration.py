from pathlib import Path
from unittest.mock import patch

import pytest

from timezone_checker.__main__ import transform, main

HERE = Path(__file__).parent


def test_entrypoint():
    with patch("sys.argv", ["timezone-checker"]):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0
    with patch("sys.argv", ["timezone-checker", "does_not_exist.py"]):
        with pytest.raises(SystemExit) as ex:
            main()
        assert ex.value.code == 0
    with patch(
        "sys.argv", ["timezone-checker", "does_not_exist.json", "--longitude", "long"]
    ):
        with pytest.raises(FileNotFoundError) as e:
            main()
        assert "No such file" in str(e.value)
    with patch(
        "sys.argv",
        ["timezone-checker", str(HERE / "already-perfect.json"), "--longitude", "long"],
    ):
        with pytest.raises(SystemExit) as ex:
            main()
        assert ex.value.code == 3


expected_json = [
    """{
    "SITE": {
        "alt": 594,
        "lat": 43.1255,
        "lon": 0.384,
        "timezone": "Europe/Pzris"
    }
}
"""
]


@pytest.mark.parametrize(
    "file_path,expected", [["fixture.py", None], ["fixture.json", expected_json]]
)
def test_transform(file_path, expected):
    fixture_file = str(HERE / file_path)
    with open(fixture_file) as f:
        content = f.readlines()
    if not expected:
        expected = content
    new_content = transform(content, "lat", "lon", "timezone")
    assert new_content == expected
