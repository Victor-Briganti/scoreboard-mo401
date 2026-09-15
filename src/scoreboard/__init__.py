import sys

from utils import parse


def main() -> None:
    path = sys.argv[1]
    _, operations = parse(path)
    print(operations)
