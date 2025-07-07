import re
from typing import Tuple, List, Dict


def parse_condition(condition: str) -> Tuple[str, str, str]:
    match = re.match(r'(\w+)\s*(=|>|<)\s*(.+)', condition)
    if not match:
        raise ValueError("Invalid condition format")
    column, operator, value = match.groups()

    if operator == '=':
        operator = '=='

    return column, operator, value


def filter_data(data: List[Dict[str, str]], condition: str) -> List[Dict[str, str]]:
    column, operator, value = parse_condition(condition)
    result = []

    for row in data:
        cell = row[column]
        if operator == '==':
            if cell == value:
                result.append(row)
        else:
            try:
                cell_value = float(cell)
                value_float = float(value)
                if operator == '>' and cell_value > value_float:
                    result.append(row)
                elif operator == '<' and cell_value < value_float:
                    result.append(row)
            except ValueError:
                continue
    return result
