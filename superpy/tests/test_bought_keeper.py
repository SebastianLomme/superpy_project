from app.date_setter import Date_setter
import os
import csv
from collections import namedtuple
from app.helper import valid_date, valid_path, date_stamp, args_date, get_id
import datetime
import pytest
import argparse
from app.bought_keeper import Bought_keeper
import pytest
import shutil

current_path = os.path.dirname(__file__)
current_path_folder = os.path.join(current_path, "files")
current_path_bought = os.path.join(current_path_folder, "bought.csv")
current_path_import_test = os.path.join(current_path_folder, "import_test.csv")
current_path_test = os.path.join(current_path_folder, "test.csv")
current_path_test_copy = os.path.join(current_path_folder, "test_copy.csv")


@pytest.fixture
def write_bought_file() -> None:
    shutil.copyfile(current_path_test, current_path_test_copy)
    yield
    print("tear_down")
    os.remove(current_path_test_copy)


@pytest.fixture
def tear_down_bought_file():
    yield
    os.remove(current_path_bought)


class Test_read_bought_to_data_csv:
    def test_read_bought_to_data_successful(self, write_bought_file):
        data = Bought_keeper(current_path_test_copy).read_bought_to_data()
        assert data == [
            {
                "id": 1,
                "product_name": "Meat",
                "buy_date": datetime.date(2021, 11, 30),
                "buy_price": 10.0,
                "expiration_date": datetime.date(2021, 12, 30),
            }
        ]

    def test_read_bought_to_data_invalled(self, write_bought_file):
        with pytest.raises(FileNotFoundError):
            Bought_keeper("incorrect_path.csv").read_bought_to_data()


class Test_read_bought_to_data:
    def test_read_bought_data_correct_types(self, write_bought_file):
        self.data = Bought_keeper(current_path_test_copy).read_bought_to_data()
        assert type(self.data[-1]["id"]) == int
        assert type(self.data[-1]["product_name"]) == str
        assert type(self.data[-1]["buy_date"]) == datetime.date
        assert type(self.data[-1]["buy_price"]) == float
        assert type(self.data[-1]["expiration_date"]) == datetime.date

    def test_make_product(self):
        product = Bought_keeper(current_path_bought).make_product(
            "Meat",
            datetime.date(2021, 11, 27),
            10.0,
            datetime.date(2021, 12, 8),
            [],
        )
        assert product == {
            "id": 1,
            "product_name": "Meat",
            "buy_date": datetime.date(2021, 11, 27),
            "buy_price": 10,
            "expiration_date": datetime.date(2021, 12, 8),
        }

    def test_make_product_error(self):
        with pytest.raises(TypeError):
            Bought_keeper(current_path_bought).make_product(
                "Meat", "2021-11-27", 10.0, "2021-12-8", [1, 2]
            )


class Test_buy_product:
    def test_buy_product_to_file(self, write_bought_file):
        Bought_keeper(current_path_test_copy).buy_product(
            "Milk",
            datetime.date(2021, 12, 5),
            2.5,
            datetime.date(2021, 12, 12),
            [{"id": 1}],
        )
        with open(current_path_test_copy, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            rows = [row for row in reader]
            assert rows[-1] == ["2;Milk;2021-12-05;2.5;2021-12-12"]


class Test_import_bought:
    def test_import_bought_product(self):
        with pytest.raises(FileNotFoundError):
            Bought_keeper(current_path_bought).import_bought_products(
                "test_file_not_exist"
            )


class Test_write_bought_file:
    def test_write_bought_file(self, tear_down_bought_file):
        Bought_keeper(current_path_bought).write_bought_file()
        assert os.path.exists(current_path_bought)


class Test_import_bought_products:
    def test_import_bought_products(self, write_bought_file):
        Bought_keeper(current_path_test_copy).import_bought_products(
            current_path_import_test
        )
        with open(current_path_test_copy, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            rows = [row for row in reader]
            assert rows[-1] == ["2;Meat;2021-11-30;10;2021-12-30"]


class Test_make_report_bought_products:
    def test_make_report_bought_products(self):
        data = [
            {
                "id": 1,
                "product_name": "Orange",
                "buy_date": datetime.date(2021, 11, 11),
                "buy_price": 0.25,
                "expiration_date": datetime.date(2021, 12, 2),
            },
            {
                "id": 2,
                "product_name": "Beef",
                "buy_date": datetime.date(2021, 11, 12),
                "buy_price": 7.5,
                "expiration_date": datetime.date(2021, 11, 30),
            },
            {
                "id": 3,
                "product_name": "Milk",
                "buy_date": datetime.date(2021, 11, 13),
                "buy_price": 0.9,
                "expiration_date": datetime.date(2021, 11, 15),
            },
            {
                "id": 4,
                "product_name": "Bread",
                "buy_date": datetime.date(2021, 11, 12),
                "buy_price": 1.5,
                "expiration_date": datetime.date(2021, 11, 14),
            },
        ]
        date = "2021-11-12"
        list_report = Bought_keeper(current_path_bought).make_report_bought_products(
            data, date
        )
        assert list_report == [
            {
                "id": 2,
                "product_name": "Beef",
                "buy_date": datetime.date(2021, 11, 12),
                "buy_price": 7.5,
                "expiration_date": datetime.date(2021, 11, 30),
            },
            {
                "id": 4,
                "product_name": "Bread",
                "buy_date": datetime.date(2021, 11, 12),
                "buy_price": 1.5,
                "expiration_date": datetime.date(2021, 11, 14),
            },
        ]

    def test_make_report_bought_products_empty_list(self):
        data = []
        date = "2021-11-12"
        list_report = Bought_keeper(current_path_bought).make_report_bought_products(
            data, date
        )
        assert list_report == []

    def test_make_report_bought_products_no_match(self):
        data = [
            {
                "id": 1,
                "product_name": "Orange",
                "buy_date": datetime.date(2021, 11, 11),
                "buy_price": 0.25,
                "expiration_date": datetime.date(2021, 12, 2),
            },
            {
                "id": 2,
                "product_name": "Beef",
                "buy_date": datetime.date(2021, 11, 12),
                "buy_price": 7.5,
                "expiration_date": datetime.date(2021, 11, 30),
            },
            {
                "id": 3,
                "product_name": "Milk",
                "buy_date": datetime.date(2021, 11, 13),
                "buy_price": 0.9,
                "expiration_date": datetime.date(2021, 11, 15),
            },
            {
                "id": 4,
                "product_name": "Bread",
                "buy_date": datetime.date(2021, 11, 12),
                "buy_price": 1.5,
                "expiration_date": datetime.date(2021, 11, 14),
            },
        ]
        date = "2021-11-15"
        list_report = Bought_keeper(current_path_bought).make_report_bought_products(
            data, date
        )
        assert list_report == []
