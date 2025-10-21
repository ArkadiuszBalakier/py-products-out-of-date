import datetime
from typing import Any


def _to_date(value: Any) -> datetime.date:
    if (isinstance(value, datetime.date)
            and not isinstance(value, datetime.datetime)):
        return value
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, str):
        # expect ISO format: 'YYYY-MM-DD'
        return datetime.date.fromisoformat(value)
    raise TypeError(
        "expiration_date must be a date, datetime, or ISO date string"
    )


def outdated_products(products: list) -> list:
    today = datetime.date.today()
    result = []
    for product in products:
        exp = _to_date(product["expiration_date"])
        if exp < today:
            result.append(product["name"])
    return result
