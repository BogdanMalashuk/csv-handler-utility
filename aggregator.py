def aggregate(data, column, op):
    values = [float(row[column]) for row in data]
    if op == 'avg':
        return round(sum(values) / len(values), 2)
    elif op == 'min':
        return min(values)
    elif op == 'max':
        return max(values)
    else:
        raise ValueError(f"Unsupported aggregation: {op}")
