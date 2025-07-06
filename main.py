import csv
from typing import List, Dict
from tabulate import tabulate
from utils import filter_data
from aggregator import aggregate
from sorter import sort_data
from parser import parse_args


def load_data(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main():
    args = parse_args()

    data = load_data(args.file)

    if args.where:
        data = filter_data(data, args.where)

    if args.aggregate:
        column, operator = args.aggregate.split('=')
        result = aggregate(data, column, operator)
        print(tabulate([[result]], headers=[operator], tablefmt="grid"))
    else:
        if args.order_by:
            column, direction = args.order_by.split('=')
            data = sort_data(data, column, direction)
        print(tabulate(data, headers='keys', tablefmt="grid"))


if __name__ == '__main__':
    main()
