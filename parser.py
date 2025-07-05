import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument('--file', required=True, help='Path to CSV file')
    parser.add_argument('--where', help='Filter condition, e.g., "price>100"')
    parser.add_argument('--aggregate', help='Aggregate column, e.g., "rating=avg"')
    parser.add_argument('--order-by', help='Ordering, e.g., "price=asc" or "rating=desc"')
    return parser.parse_args()
