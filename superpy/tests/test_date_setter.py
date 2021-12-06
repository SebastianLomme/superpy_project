import os
from collections import namedtuple
import datetime
import pytest
import pytest

from app.date_setter import Date_setter

current_path = os.path.dirname(__file__)
current_path_folder = os.path.join(current_path, "files")


class Test_Date_setter:
    today = datetime.datetime.today().date().strftime("%Y-%m-%d")
    current_path_today = os.path.join(current_path_folder, "today_test.txt")

    @pytest.fixture
    def set_day_file(self):
        with open(self.current_path_today, "w") as file:
            file.write("2021-11-30")

    @pytest.fixture
    def remove_today_file(self):
        os.remove(self.current_path_today)

    def test_date_setter(self, set_day_file):
        date = str(Date_setter(self.current_path_today).read_date_from_file())
        assert date == "2021-11-30"

    def test_date_setter_days(self, set_day_file):
        date = str(Date_setter(
            self.current_path_today).set_new_date_whit_days_input(5))
        assert date == "2021-12-05"

    def test_set_date_today(self):
        date = str(Date_setter(self.current_path_today).set_date_today())
        assert date == self.today

    def test_args_today(self):
        args_tuple = namedtuple("args", "today days")
        args = args_tuple(True, None)
        date = Date_setter(self.current_path_today).set_date_args(args)
        assert date == self.today

    def test_args_days(self, set_day_file):
        args_tuple = namedtuple("args", "today days")
        args = args_tuple(False, 5)
        date = Date_setter(self.current_path_today).set_date_args(args)
        assert date == "2021-12-05"

    def test_args_days_none(self, set_day_file):
        args_tuple = namedtuple("args", "today days")
        args = args_tuple(False, None)
        date = Date_setter(self.current_path_today).set_date_args(args)
        assert date == "2021-11-30"

    def test_args_days_no_file(self, remove_today_file):
        args_tuple = namedtuple("args", "today days")
        args = args_tuple(False, None)
        date = Date_setter(self.current_path_today).set_date_args(args)
        assert date == self.today
