from app.date_setter import Date_setter

import os
from collections import namedtuple
from app.helper import valid_date, valid_path, date_stamp, args_date
import datetime
import pytest
import argparse

current_path = os.path.dirname(__file__)

def test_valid_date():
    date = valid_date("2021-11-20")
    assert isinstance(date, datetime.date)

def test_valid_date_fails():
    with pytest.raises(argparse.ArgumentTypeError):
        valid_date("11-05-2021")
        


class Test_Date_setter:

    current_path_today = os.path.join(current_path, "today_test.txt")
    def test_date_setter(self):
        date = str(Date_setter(self.current_path_today).read_date_from_file())
        assert date == "2021-11-26"

    def test_date_setter_days(self):
        date = str(Date_setter(self.current_path_today).set_new_date_whit_days_input(5))
        assert date == "2021-12-01"

    def test_set_date_today(self):
        date = str(Date_setter(self.current_path_today).set_date_today())
        assert date == "2021-11-26"

class Test_Valid_Path_Error:
    def test_valid_path_exists(self):
        with pytest.raises(argparse.ArgumentTypeError):
            path = valid_path("test_file_not_exists")
    
    def test_valid_path_not_exists(self):
        test_path = os.path.join(current_path, "today_test.txt")
        path = valid_path("today_test.txt", current_path)
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