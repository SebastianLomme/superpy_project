import argparse
from helper import valid_date
import datetime
from helper import valid_path

parser = argparse.ArgumentParser(description="Keep track of your stock", prog="SuperPy", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "-a",
    "--advance-time",
    metavar="nr_days",
    type=int,
    dest="days",
    help="Enter number of days you wood like to add",
)
# parser.add_argument(
#     "-d",
#     "--delimiter",
#     action="store",
#     choices=["comma", "semicolon", "tab", "space", "pipe"],
#     help="Set your delimiter",
# )
parser.add_argument("-t", "--today", action="store_true", help="Set date to today")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

subparser = parser.add_subparsers(dest="command")

# start_parser = subparser.add_parser("start", help="set date to today")

import_bought_parser = subparser.add_parser("import", help="import all items from a csv from given path")
import_bought_parser.add_argument("path", type=valid_path, help="path to file")


report_parser = subparser.add_parser(
    "report",
    help="show report for choice from revenue, inventory, profit, expired. Use report -h for more information",
)

report_parser.add_argument(
    "report",
    help="show report for choice from revenue, inventory, profit, expired. Use report -h for more information",
    type=str,
    choices = ["revenue", "inventory", "profit", "expired"]
)

# report_group = report_parser.add_mutually_exclusive_group()
# report_group.add_argument(
#     "--revenue",
#     dest="report_revenue",
#     action="store_true",
#     help="show a report of revenue for the set date",
# )

# report_group.add_argument(
#     "--inventory",
#     dest="report_inventory",
#     action="store_true",
#     help="show a report of inventory for the set date",
# )

# report_group.add_argument(
#     "--profit",
#     dest="report_profit",
#     action="store_true",
#     help="show a report of profit for the set date",
# )

# report_group.add_argument(
#     "--expired",
#     dest="report_expired",
#     action="store_true",
#     help="show a report of expired products for the set date",
# )

report_date_group = report_parser.add_mutually_exclusive_group()
report_date_group.add_argument(
    "--now",
    default=True,
    dest="report_date",
    action="store_true",
    help="Sets date for report as today",
)
report_date_group.add_argument(
    "--yesterday",
    dest="report_date",
    action="store_false",
    help="Sets date for report as yesterday",
)
report_date_group.add_argument(
    "--date",
    dest="report_date",
    type=valid_date,
    action="store",
    help="sets date for report as as given date format YYYY-MM-DD",
)

report_to_date_group = report_parser.add_mutually_exclusive_group()
report_to_date_group.add_argument(
    "--to_now",
    default="",
    dest="report_to_date",
    action="store_true",
    help="Sets date for report as today",
)
report_to_date_group.add_argument(
    "--to_yesterday",
    dest="report_to_date",
    action="store_false",
    help="Sets date for report as yesterday",
)
report_to_date_group.add_argument(
    "--to_date",
    dest="report_to_date",
    type=valid_date,
    action="store",
    help="sets date for report as as given date format YYYY-MM-DD",
)



report_parser.add_argument(
    "--export",
    dest="report_export",
    type=str,
    action="store",
    help="Enter the name for the file to export report to csv file, YYYY-MM-DD.csv will be added to filename",
)


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
