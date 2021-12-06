from datetime import datetime
import argparse
import os
from rich.console import Console

console = Console()


current_path = os.getcwd()


def get_id(list_data):
    if len(list_data) == 0:
        return 1
    else:
        return int(list_data[-1]["id"]) + 1


def valid_date(s):
    try:
        return date_stamp(s)
    except ValueError:
        msg = f"👎 Error not a valid date: {s} use format YYYY-MM-DD"
        raise argparse.ArgumentTypeError(msg)


def valid_path(s, path=current_path):
    path = os.path.join(path, s)
    print("path: {}".format(path))
    if os.path.exists(path):
        return path
    else:
        msg = f"👎 Error {path} is not a valid file!!!!"
        raise argparse.ArgumentTypeError(msg)


def args_date(date, today, yesterday):
    if date == True:
        return today
    elif date == False:
        return yesterday
    elif date == "":
        return ""
    else:
        return date.strftime("%Y-%m-%d")


def date_stamp(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        msg = f"👎 Error not a valid date: {date} use format YYYY-MM-DD"
        raise ValueError(msg)
