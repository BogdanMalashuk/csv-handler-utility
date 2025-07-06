AGGREGATIONS = {
    'avg': lambda vals: round(sum(vals) / len(vals), 2),
    'min': min,
    'max': max,
}


def aggregate(data, column, operator):
    values = [float(row[column]) for row in data]
    if operator not in AGGREGATIONS:
        raise ValueError(f"Unsupported aggregation: {operator}")
    return AGGREGATIONS[operator](values)
