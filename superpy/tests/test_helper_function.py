import os
from superpy.app.helper import valid_date, valid_path, date_stamp, args_date, get_id
import datetime
import pytest
import argparse
import pytest

current_path = os.path.dirname(__file__)
current_path_folder = os.path.join(current_path, "files")


class Test_valid_date:
    def test_valid_date(self):
        date = valid_date("2021-11-20")
        assert isinstance(date, datetime.date)

    def test_valid_date_fails(self):
        with pytest.raises(argparse.ArgumentTypeError):
            valid_date("11-05-2021")


class Test_Valid_Path:
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


class Test_get_id:
    def test_get_id(self):
        assert get_id([{"id": 1}, {"id": 2}]) == 3

    def test_get_id_empty_list(self):
        assert get_id([]) == 1


class Test_args_date:
    def test_args_date_today(self):
        test_date = args_date(True, "2021-11-26", "2021-11-25")
        assert test_date == "2021-11-26"

    def test_args_date_yesterday(self):
        test_date = args_date(False, "2021-11-26", "2021-11-25")
        assert test_date == "2021-11-25"

    def test_args_date_date(self):
        test_date = args_date(date_stamp("2021-11-20"),
                              "2021-11-26", "2021-11-25")
        assert test_date == "2021-11-20"

    def test_args_date_date_empty_string(self):
        test_date = args_date("", "2021-11-26", "2021-11-25")
        assert test_date == ""

    def test_args_date_value_error(self):
        with pytest.raises(ValueError):
            args_date(date_stamp("20-11-2021"), "2021-11-26", "2021-11-25")
