import csv
from typing import Dict, Callable, Any


def parse_example_csv_to_dict(
    file_path: str = "example.csv",
    key_col: str = "category",
    value_col: str = "value",
    cast_value: Callable[[str], Any] = int,
) -> Dict[str, Any]:
    """
    Parse the example CSV into a dict mapping key_col -> value_col.

    Args:
        file_path: Path to the CSV file.
        key_col: Column to use as keys (default: 'category').
        value_col: Column to use as values (default: 'value').
        cast_value: Function to cast value strings (default: int).

    Returns:
        Dict of {key: value}.
    """
    result: Dict[str, Any] = {}
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if key_col not in reader.fieldnames or value_col not in reader.fieldnames:
            raise ValueError(
                f"CSV must contain columns {key_col!r} and {value_col!r}. "
                f"Found: {reader.fieldnames}"
            )
        for row in reader:
            key = str(row[key_col]).strip()
            raw_val = row[value_col]
            value = cast_value(raw_val) if raw_val is not None else None
            result[key] = value
    return result


if __name__ == "__main__":
    data = parse_example_csv_to_dict()
    print("Parsed dict:", data)
