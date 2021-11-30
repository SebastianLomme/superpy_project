from app.date_setter import Date_setter

import os
from collections import namedtuple
from app.helper import valid_date, valid_path, date_stamp, args_date
import datetime
import pytest
import argparse
from app.bought_keeper import Bought_keeper

current_path = os.path.dirname(__file__)
current_path_folder = os.path.join(current_path, "files")
current_path_bought = os.path.join(current_path_folder, "bought.csv")


def test_valid_date():
    date = valid_date("2021-11-20")
    assert isinstance(date, datetime.date)


def test_valid_date_fails():
    with pytest.raises(argparse.ArgumentTypeError):
        valid_date("11-05-2021")


class Test_Date_setter:
    today = datetime.datetime.today().date()
    today_plus_five_days = today + datetime.timedelta(days=5)

    current_path_today = os.path.join(current_path_folder, "today_test.txt")

    def test_date_setter(self):
        date = str(Date_setter(self.current_path_today).read_date_from_file())
        assert date == self.today.strftime("%Y-%m-%d")

    def test_date_setter_days(self):
        date = str(Date_setter(self.current_path_today).set_new_date_whit_days_input(5))
        assert date == self.today_plus_five_days.strftime("%Y-%m-%d")

    def test_set_date_today(self):
        date = str(Date_setter(self.current_path_today).set_date_today())
        assert date == self.today.strftime("%Y-%m-%d")


class Test_Valid_Path_Error:
    def test_valid_path_not_exists(self):
        with pytest.raises(argparse.ArgumentTypeError):
            path = valid_path("test_file_not_exists")

    def test_valid_path_exists(self):
        test_path = os.path.join(current_path_folder, "today_test.txt")
        path = valid_path("today_test.txt", current_path_folder)
        assert path == test_path


class Test_date_stamp:
    def test_valid_date_stamp_format(self):
        assert isinstance(date_stamp("2021-11-20"), datetime.date)

    def test_invalid_date_stamp_format(self):
        with pytest.raises(ValueError):
            date_stamp("20-11-2021")


class Test_args_date:
    def test_args_date_today(self):
        test_date = args_date(True, "2021-11-26", "2021-11-25")
        assert test_date == "2021-11-26"

    def test_args_date_yesterday(self):
        test_date = args_date(False, "2021-11-26", "2021-11-25")
        assert test_date == "2021-11-25"

    def test_args_date_date(self):
        test_date = args_date(date_stamp("2021-11-20"), "2021-11-26", "2021-11-25")
        assert test_date == "2021-11-20"

    def test_args_date_value_error(self):
        with pytest.raises(ValueError):
            args_date(date_stamp("20-11-2021"), "2021-11-26", "2021-11-25")


class Test_read_bought_to_data:
    data = []

    def test_read_bought_data_correct(self):
        data = Bought_keeper(current_path_bought).read_bought_to_data()
        assert data == [
            {
                "id": 1,
                "product_name": "Salade",
                "buy_date": datetime.date(2021, 11, 27),
                "buy_price": 2.5,
                "expiration_date": datetime.date(2021, 12, 5),
            },
            {
                "id": 2,
                "product_name": "Beef",
                "buy_date": datetime.date(2021, 11, 30),
                "buy_price": 5,
                "expiration_date": datetime.date(2021, 12, 10),
            },
        ]

    def test_read_bought_data_correct_types(self):
        self.data = Bought_keeper(current_path_bought).read_bought_to_data()
        assert type(self.data[-1]["id"]) == int
        assert type(self.data[-1]["product_name"]) == str
        assert type(self.data[-1]["buy_date"]) == datetime.date
        assert type(self.data[-1]["buy_price"]) == float
        assert type(self.data[-1]["expiration_date"]) == datetime.date

    def test_buy_product(self):
        product = Bought_keeper(current_path_bought).make_product(
            "Meat",
            datetime.date(2021, 11, 27),
            10.0,
            datetime.date(2021, 12, 8),
            [{"id": 1}],
        )
        assert product == {
            "id": 2,
            "product_name": "Meat",
            "buy_date": datetime.date(2021, 11, 27),
            "buy_price": 10,
            "expiration_date": datetime.date(2021, 12, 8),
        }
        with pytest.raises(TypeError):
            Bought_keeper(current_path_bought).make_product(
                "Meat", datetime.date(2021, 11, 27), 10.0, datetime.date(2021, 12, 8), 1
            )


class Test_import_bought:
    def test_import_bought_product(self):
        with pytest.raises(FileNotFoundError):
            Bought_keeper(current_path_bought).import_bought_products(
                "test_file_not_exist"
            )
