from typing import List, Dict


def sort_data(data, column, direction) -> List[Dict[str, str]]:
    reverse = direction.lower() == 'desc'
    try:
        return sorted(data, key=lambda x: float(x[column]), reverse=reverse)
    except ValueError:
        return sorted(data, key=lambda x: x[column], reverse=reverse)
