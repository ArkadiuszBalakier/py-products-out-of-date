import datetime
from typing import List, Dict, Any

import unittest.mock


from app.main import outdated_products


MOCK_PATH_DATE_TODAY = "app.main.datetime.date.today"

EXAMPLE_PRODUCTS: List[Dict[str, Any]] = [
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


class TestOutdatedProducts:


    @unittest.mock.patch(MOCK_PATH_DATE_TODAY)
    def test_example_scenario(self: object, mock_today: unittest.mock.MagicMock) -> None:
        today_date = datetime.date(2022, 2, 2)
        mock_today.return_value = today_date

        expected = ["duck"]
        result = outdated_products(EXAMPLE_PRODUCTS)

        assert result == expected


    @unittest.mock.patch(MOCK_PATH_DATE_TODAY)
    def test_day_before_all_expired(self: object, mock_today: unittest.mock.MagicMock) -> None:
        today_date = datetime.date(2022, 2, 11)
        mock_today.return_value = today_date

        expected = ["salmon", "chicken", "duck"]
        result = outdated_products(EXAMPLE_PRODUCTS)

        assert result == expected


    @unittest.mock.patch(MOCK_PATH_DATE_TODAY)
    def test_none_outdated(self: object, mock_today: unittest.mock.MagicMock) -> None:
        today_date = datetime.date(2022, 1, 31)
        mock_today.return_value = today_date

        expected = []
        result = outdated_products(EXAMPLE_PRODUCTS)

        assert result == expected


    @unittest.mock.patch(MOCK_PATH_DATE_TODAY)
    def test_two_outdated(self: object, mock_today: unittest.mock.MagicMock) -> None:
        today_date = datetime.date(2022, 2, 6)
        mock_today.return_value = today_date

        expected = ["chicken", "duck"]
        result = outdated_products(EXAMPLE_PRODUCTS)

        assert sorted(result) == sorted(expected)
