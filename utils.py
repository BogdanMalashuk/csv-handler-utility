import re


def parse_condition(condition):
    match = re.match(r'(\w+)\s*(=|>|<)\s*(.+)', condition)
    if not match:
        raise ValueError("Invalid condition format")
    col, operator, val = match.groups()

    if operator == '=':
        operator = '=='

    return col, operator, val
