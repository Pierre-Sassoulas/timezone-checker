# timezone-checker

Little pre-commit script that fix timezone in your configuration file

[![PyPI version](https://badge.fury.io/py/remove-empty-comment.svg)](https://badge.fury.io/py/timezone-checker)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> You can check the timezone if you give latitude and longitude.

## Installation

```yaml
-   repo: https://github.com/Pierre-Sassoulas/timezone-checker/
    rev: 1.1.0
    hooks:
    - id: timezone-checker
      args: [--longitude, "lon", --latitude, "lat", --timezone, "tz"]
```

## Use

```
usage: timezone-checker [-h] [-c MEANINGLESS_CHARACTERS] [FILES [FILES ...]]

positional arguments:
  FILES                 File names to modify

optional arguments:
  -h, --help            show this help message and exit
  -c MEANINGLESS_CHARACTERS, --meaningless-characters MEANINGLESS_CHARACTERS
                        Characters that have no meaning alone. If there are alone in a comment, it will be removed.
```

## Before

```json
```

## After

```json

```