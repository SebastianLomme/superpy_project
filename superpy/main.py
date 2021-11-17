# Imports
from datetime import datetime, timedelta
import os
from rich.console import Console
from rich.table import Table


from parser import args
from helper import get_id
from date_setter import Date_setter
from bought_keeper import Bought_keeper
from sold_keeper import Sold_keeper
from inventory_keeper import Inventory_keeper


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


current_path = os.path.dirname(__file__)
current_path_bought = os.path.join(current_path, "bought.csv")
current_path_stock = os.path.join(current_path, "stock_list.csv")
current_path_sold = os.path.join(current_path, "sold_list.csv")
current_path_today = os.path.join(current_path, "today.txt")
data_stock = []
console = Console()


def main():
    today = str(Date_setter(current_path_today, args))
    yesterday = (datetime.strptime(today, "%Y-%m-%d").date() - timedelta(days=1)).strftime("%Y-%m-%d")
    print("yesterday: ", type(yesterday), yesterday)
    bought_keeper = Bought_keeper(current_path_bought)
    data_bought = bought_keeper.read_bought_to_data()
    sold_keeper = Sold_keeper(current_path_sold)
    data_sold = sold_keeper.read_sold_list()
    inventory_keeper = Inventory_keeper(current_path_stock)

    console.print(
        "Command: ",
        args.command, args
    )
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
        if args.report_date == True:
            inventory_keeper.make_report_stock(today, data_bought, data_sold)
        elif args.report_date == False:
            inventory_keeper.make_report_stock(yesterday, data_bought, data_sold)
        else:
            inventory_keeper.make_report_stock(args.report_date.strftime("%Y-%m-%d"), data_bought, data_sold)
    data_bought = bought_keeper.read_bought_to_data()
    data_stock = inventory_keeper.get_stock(today, data_bought, data_sold)
    inventory_keeper.make_report_expired(today, data_bought, data_sold)
    

if __name__ == "__main__":
    main()
