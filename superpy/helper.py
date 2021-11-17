from datetime import datetime, date
import argparse


def get_id(list_data):
    if len(list_data) == 0:
        return 1
    else:
        return int(list_data[-1]["id"]) + 1


def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "not a valid date: {0!r} use format YYYY-MM-DD".format(s)
        raise argparse.ArgumentTypeError(msg)
