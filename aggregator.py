from typing import List, Dict

# Добавление новых функций для агрегации через словарь

AGGREGATIONS = {
    'avg': lambda vals: round(sum(vals) / len(vals), 2),
    'min': min,
    'max': max,
}


def aggregate(data: List[Dict[str, str]], column: str, operator: str):
    values = [float(row[column]) for row in data]
    if operator not in AGGREGATIONS:
        raise ValueError(f"Unsupported aggregation: {operator}")
    return AGGREGATIONS[operator](values)
