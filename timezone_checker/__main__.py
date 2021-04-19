"""Check the timezone in configuration file where latitude and longitude are given.
Used by pre-commit."""

import argparse
import json
import sys
from typing import List, Union, Dict


def main(argv: Union[List[str], None] = None) -> int:
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        metavar="FILES",
        help="File names to modify",
    )
    parser.add_argument(
        "--latitude",
        default="lat",
        help="Value to search for latitude in configuration file",
    )
    parser.add_argument(
        "--longitude",
        default="lon",
        help="Value to search for longitude in configuration file",
    )
    parser.add_argument(
        "--timezone",
        default="timezone",
        help="Value to search for timezone in configuration file",
    )
    args = parser.parse_args(argv)
    for file_name in args.filenames:
        try:
            clean(file_name, args.latitude, args.longitude, args.timezone)
        except UnicodeDecodeError:
            pass
    sys.exit(0)


def clean(file_name: str, latitude: str, longitude: str, timezone: str):
    if not file_name.endswith("json"):
        return
    with open(file_name, encoding="utf8") as f:
        content = json.load(f)
    if not need_to_be_checked(content, latitude, longitude, timezone):
        return
    print(f"Checking '{file_name}'")
    new_content = transform(content, latitude, longitude, timezone)
    with open(file_name, "w", encoding="utf8") as f:
        json.dump(new_content, f, sort_keys=False, indent=4)


def need_to_be_checked(content: Dict, latitude: str, longitude: str, timezone: str):
    if isinstance(content, dict):
        return all(x in content for x in [latitude, longitude, timezone]) or any(
            need_to_be_checked(v, latitude, longitude, timezone)
            for v in content.values()
        )
    return False


def transform(
    content: List[str], latitude: str, longitude: str, timezone: str
) -> List[str]:
    new_content: List[str] = []
    for line in content:
        print(line)
    return content


if __name__ == "__main__":
    main()
