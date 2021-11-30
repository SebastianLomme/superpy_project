import os
from rich.console import Console

current_path = os.getcwd()
current_path_files = os.path.join(current_path, "files")
current_path_bought = os.path.join(current_path_files, "bought.csv")
current_path_stock = os.path.join(current_path_files, "stock_list.csv")
current_path_sold = os.path.join(current_path_files, "sold_list.csv")
current_path_today = os.path.join(current_path_files, "today.txt")
console = Console()
