from datetime import datetime, date
import argparse
import os
from variable import console


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
        msg = "👎 Error not a valid date: {0!r} use format YYYY-MM-DD".format(s)
        raise argparse.ArgumentTypeError(msg)


def valid_path(s, path=current_path):
    path = os.path.join(path, s)
    print("path: {}".format(path))
    if os.path.exists(path):
        return path
    else:
        msg = "👎 Error not a valid file!!!!"
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
        msg = "👎 Error not a valid date: {0!r} use format YYYY-MM-DD".format(date)
        raise ValueError(msg)
