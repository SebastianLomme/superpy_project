import argparse

parser = argparse.ArgumentParser(
    description="enter de numbers of days you wood like to add ", prog="SuperPy"
)
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
parser.add_argument("-t", "--today", action="store_true", help="Set to today")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")
subparser = parser.add_subparsers(dest="command")

sell_parser = subparser.add_parser("sell", help="register purchased product")
sell_parser.add_argument("--id", type=int, required=True, help="bought id")
sell_parser.add_argument("--sell_price", type=float, required=True, help="price")


buy_parser = subparser.add_parser("buy", help="register sold product")
buy_parser.add_argument("--product_name", type=str, required=True, help="product name")
buy_parser.add_argument("--buy_date", type=str, required=True, help="buy date")
buy_parser.add_argument("--buy_price", type=float, required=True, help="buy price")
buy_parser.add_argument(
    "--expiration_date", type=str, required=True, help="expiration date"
)

args = parser.parse_args()
