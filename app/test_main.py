import datetime
from pytest import MonkeyPatch


from app.main import outdated_products


MOCK_PATH_DATE_TODAY = "app.main.datetime.date.today"

EXAMPLE_PRODUCTS = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }
]


def test_example_scenario(monkeypatch: MonkeyPatch) -> None:
    today_date = datetime.date(2022, 2, 2)
    monkeypatch.setattr(MOCK_PATH_DATE_TODAY, lambda: today_date)
    expected = ["duck"]
    result = outdated_products(EXAMPLE_PRODUCTS)
    assert result == expected


def test_day_before_all_expired(monkeypatch: MonkeyPatch) -> None:
    today_date = datetime.date(2022, 2, 11)
    monkeypatch.setattr(MOCK_PATH_DATE_TODAY, lambda: today_date)
    expected = ["salmon", "chicken", "duck"]
    result = outdated_products(EXAMPLE_PRODUCTS)

    assert result == expected


def test_none_outdated(monkeypatch: MonkeyPatch) -> None:
    today_date = datetime.date(2022, 1, 31)
    monkeypatch.setattr(MOCK_PATH_DATE_TODAY, lambda: today_date)
    expected = []
    result = outdated_products(EXAMPLE_PRODUCTS)

    assert result == expected
