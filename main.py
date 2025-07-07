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


def main() -> None:
    args = parse_args()

    try:
        data = load_data(args.file)

        if args.where:
            data = filter_data(data, args.where)

        if args.aggregate:
            column, operator = args.aggregate.split('=')
            result = aggregate(data, column, operator)
            print(tabulate([[result]], headers=[operator], tablefmt="psql"))
        else:
            if args.order_by:
                column, direction = args.order_by.split('=')
                if direction.lower() not in ("asc", "desc"):
                    raise ValueError("Сортировка должна быть 'asc' или 'desc'")
                data = sort_data(data, column, direction)

            print(tabulate(data, headers="keys", tablefmt="psql"))

    except FileNotFoundError:
        print(f"[Ошибка] Файл не найден: {args.file}")
    except KeyError as e:
        print(f"[Ошибка] Колонка не найдена: {e}")
    except ValueError as e:
        print(f"[Ошибка] Неверный ввод: {e}")
    except Exception as e:
        print(f"[Ошибка] Что-то пошло не так: {e}")


if __name__ == '__main__':
    main()
