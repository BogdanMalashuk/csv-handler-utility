AGGREGATIONS = {
    'avg': lambda vals: round(sum(vals) / len(vals), 2),
    'min': min,
    'max': max,
}


def aggregate(data, column, op):
    values = [float(row[column]) for row in data]
    if op not in AGGREGATIONS:
        raise ValueError(f"Unsupported aggregation: {op}")
    return AGGREGATIONS[op](values)
