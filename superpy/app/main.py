# Imports
from datetime import datetime, timedelta
import os
from rich.console import Console
from rich.table import Table


from parser import args
from helper import get_id, args_date
from date_setter import Date_setter
from bought_keeper import Bought_keeper
from sold_keeper import Sold_keeper
from inventory_keeper import Inventory_keeper
from revenue_keeper import Revenue_keeper


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


current_path = os.path.dirname(__file__)
current_path_bought = os.path.join(current_path, "../files/bought.csv")
current_path_stock = os.path.join(current_path, "../files/stock_list.csv")
current_path_sold = os.path.join(current_path, "../files/sold_list.csv")
current_path_today = os.path.join(current_path, "../files/today.txt")
print(current_path, current_path_today)
data_stock = []
console = Console()


def add(num1, num2):
    return num1 + num2


def main():
    today = str(Date_setter(current_path_today, args))
    yesterday = (
        datetime.strptime(today, "%Y-%m-%d").date() - timedelta(days=1)
    ).strftime("%Y-%m-%d")
    bought_keeper = Bought_keeper(current_path_bought)
    data_bought = bought_keeper.read_bought_to_data()
    sold_keeper = Sold_keeper(current_path_sold)
    data_sold = sold_keeper.read_sold_list()
    inventory_keeper = Inventory_keeper(current_path_stock)

    console.print("Command: ", args)
    if args.command == "sell":
        data_stock = inventory_keeper.get_stock(today, data_bought, data_sold)
        sold_keeper.sell_product(
            args.product_name, args.sell_price, today, data_sold, data_stock
        )
        data_sold = sold_keeper.read_sold_list()

    elif args.command == "buy":
        bought_keeper.buy_product(
            args.product_name,
            args.buy_date,
            args.buy_price,
            args.expiration_date,
            data_bought,
        )
    elif args.command == "report":
        if args.report == "inventory":
            date = args_date(args.report_date, today, yesterday)
            inventory_data = inventory_keeper.make_report_stock(
                date, data_bought, data_sold
            )
            if args.report_export != None:
                inventory_keeper.export_report_csv(
                    inventory_data, f"{args.report_export}_{date}.csv"
                )
        elif args.report == "revenue":
            date = args_date(args.report_date, today, yesterday)
            to_date = args_date(args.report_to_date, today, yesterday)
            revenue = Revenue_keeper(data_sold).get_revenue(date, to_date)
            Revenue_keeper(data_sold).print_revenue(revenue)
            if args.report_export != None:
                inventory_keeper.export_report_csv(
                    revenue, f"{args.report_export}_{date}.csv"
                )
        elif args.report == "profit":
            print("profit")
        elif args.report == "expired":
            date = args_date(args.report_date, today, yesterday)
            expired_data = inventory_keeper.make_report_expired(
                date, data_bought, data_sold
            )
            if args.report_export != None:
                inventory_keeper.export_report_csv(
                    expired_data, f"{args.report_export}_{date}.csv"
                )
    elif args.command == "import":
        bought_keeper.import_bought_products(args.path)

    data_bought = bought_keeper.read_bought_to_data()
    data_stock = inventory_keeper.get_stock(today, data_bought, data_sold)


if __name__ == "__main__":
    main()
