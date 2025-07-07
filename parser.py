import argparse
from argparse import Namespace
import sys


class CustomArgumentParser(argparse.ArgumentParser):  # кастомные ошибки в понятном формате
    def error(self, message):
        print(f"[Ошибка аргумента] {message}")
        sys.exit(2)


def parse_args() -> Namespace:
    parser = CustomArgumentParser(description="CSV Handler Utility")
    parser.add_argument('--file', required=True, help='Path to CSV file')
    parser.add_argument('--where', help='Filter condition, e.g., "price>100"')
    parser.add_argument('--aggregate', help='Aggregate column, e.g., "rating=avg"')
    parser.add_argument('--order-by', help='Ordering, e.g., "price=asc" or "rating=desc"')
    return parser.parse_args()
