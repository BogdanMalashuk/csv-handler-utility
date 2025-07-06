import re


def parse_condition(condition):
    match = re.match(r'(\w+)\s*(=|>|<)\s*(.+)', condition)
    if not match:
        raise ValueError("Invalid condition format")
    col, operator, val = match.groups()

    if operator == '=':
        operator = '=='

    return col, operator, val


def filter_data(data, condition):
    col, op, val = parse_condition(condition)
    result = []

    for row in data:
        cell = row[col]
        if op == '==':
            if cell == val:
                result.append(row)
        else:
            try:
                cell_value = float(cell)
                val_float = float(val)
                if op == '>' and cell_value > val_float:
                    result.append(row)
                elif op == '<' and cell_value < val_float:
                    result.append(row)
            except ValueError:
                continue
    return result
