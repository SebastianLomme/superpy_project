import argparse
from helper import valid_date
import datetime

parser = argparse.ArgumentParser(description="Keep track of your stock", prog="SuperPy")
parser.add_argument(
    "-a",
    "--advance-time",
    metavar="nr_days",
    type=int,
    dest="days",
    help="Enter number of days you wood like to add",
)
parser.add_argument(
    "-d",
    "--delimiter",
    action="store",
    choices=["comma", "semicolon", "tab", "space", "pipe"],
    help="Set your delimiter",
)
parser.add_argument("-t", "--today", action="store_true", help="Set date to today")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")
subparser = parser.add_subparsers(dest="command")

start_parser = subparser.add_parser("start", help="set date to today")

report_parser = subparser.add_parser("report", help="show a report of inventory for the set date")
report_group = report_parser.add_mutually_exclusive_group()
report_group.add_argument("--now", default=True, dest="report_date",  action="store_true", help="test")
report_group.add_argument("--yesterday", dest="report_date",  action="store_false", help="test")
report_group.add_argument("--date", dest="report_date", type=valid_date, action="store", help="test")



sell_parser = subparser.add_parser("sell", help="register purchased product")
sell_parser.add_argument("--product_name", type=str, required=True, help="product_name")
sell_parser.add_argument("--sell_price", type=float, required=True, help="price")


buy_parser = subparser.add_parser("buy", help="register sold product")
buy_parser.add_argument("--product_name", type=str, required=True, help="product name")
buy_parser.add_argument(
    "--buy_date", type=valid_date, required=True, help="buy date format YYYY-MM-DD"
)
buy_parser.add_argument("--buy_price", type=float, required=True, help="buy price")
buy_parser.add_argument(
    "--expiration_date",
    type=valid_date,
    required=True,
    help="expiration date format YYYY-MM-DD (inclusive)",
)

args = parser.parse_args()
