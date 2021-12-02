import os
from rich.console import Console
from datetime import timedelta, datetime
from app.parsers import args
from app.date_setter import Date_setter
from app.bought_keeper import Bought_keeper
from app.sold_keeper import Sold_keeper
from app.inventory_keeper import Inventory_keeper


current_path = os.getcwd()
current_path_files = os.path.join(current_path, "files")
current_path_bought = os.path.join(current_path_files, "bought.csv")
current_path_stock = os.path.join(current_path_files, "stock_list.csv")
current_path_sold = os.path.join(current_path_files, "sold_list.csv")
current_path_today = os.path.join(current_path_files, "today.txt")
console = Console()

bought_keeper = Bought_keeper(current_path_bought)
sold_keeper = Sold_keeper(current_path_sold)
inventory_keeper = Inventory_keeper(current_path_stock)
today = str(Date_setter(current_path_today).set_date_args(args))
yesterday = (
    datetime.strptime(today, "%Y-%m-%d").date()- timedelta(days=1)
    ).strftime("%Y-%m-%d")
    
# data_bought = bought_keeper.read_bought_to_data()
# data_sold = sold_keeper.read_sold_list()