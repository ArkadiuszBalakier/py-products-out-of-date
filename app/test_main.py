import datetime
from unittest.mock import patch


from app.main import outdated_products


def test_outdated_products_return_list_of_expaired_products_names() -> None:
    with patch("app.main.datetime.date") as mock_date :
        mock_date.today.return_value = datetime.date(2025, 1, 1)
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)
        products = [
            {
                "name": "salmon",
                "expiration_date": mock_date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": mock_date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": mock_date(2022, 2, 1),
                "price": 160
            }
        ]
        assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_product_with_expiration_date_equals_today_is_not_outdated() -> None:
    with patch("app.main.datetime.date") as mock_date :
        mock_date.today.return_value = datetime.date(2022, 2, 1)
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)
        products = [
            {
                "name": "salmon",
                "expiration_date": mock_date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": mock_date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": mock_date(2022, 2, 1),
                "price": 160
            }
        ]
        assert outdated_products(products) == []
