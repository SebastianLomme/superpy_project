import os
import csv
from datetime import date, timedelta, datetime

current_path = os.path.dirname(__file__)
current_path_bought = os.path.join(current_path, "bought.csv")
current_path_stock = os.path.join(current_path, "stock_list.csv")
current_path_sold = os.path.join(current_path, "sold_list.csv")
current_path_today = os.path.join(current_path, "today.txt")
data = []
data_sold = []
data_stock = []
delimiter = ";"


def read_bought_to_data():
    data.clear()
    with open(current_path_bought, "r", newline="") as file:
        reader = csv.DictReader(
            file,
            delimiter=";",
            fieldnames=[
                "id",
                "product_name",
                "buy_date",
                "buy_price",
                "expiration_data",
            ],
        )
        # Skip over header field
        next(reader)
        for row in reader:
            # [id, product_name, buy_date, buy_price, expiration_data]
            id = int(row["id"])
            product_name = str(row["product_name"])
            buy_date = datetime.strptime(row["buy_date"], "%Y-%m-%d")
            buy_price = float(row["buy_price"])
            expiration_data = datetime.strptime(row["expiration_data"], "%Y-%m-%d")
            data.append(
                {
                    "id": id,
                    "product_name": product_name,
                    "buy_date": buy_date,
                    "buy_price": buy_price,
                    "expiration_data": expiration_data,
                }
            )


def read_sold_list():
    if os.path.exists(current_path_sold):
        with open(current_path_sold, "r", newline="") as sold_list:
            fieldnames = ["id", "bought_id", "sell_date", "sell_price"]
            read_sold_list = csv.DictReader(
                sold_list, delimiter=delimiter, fieldnames=fieldnames
            )
            next(read_sold_list)
            for line in read_sold_list:
                data_sold.append(line)
    else:
        with open(current_path_sold, "w", newline="") as sold_list:
            fieldnames = ["id", "bought_id", "sell_date", "sell_price"]
            writer_sold_list = csv.DictWriter(
                sold_list, delimiter=delimiter, fieldnames=fieldnames
            )
            writer_sold_list.writeheader()
            for line in data_sold:
                writer_sold_list.write(line)


def reader_stock_list():
    if os.path.exists(current_path_stock):
        with open(current_path_stock, "r", newline="") as stock_list:
            reader_stock_list = csv.DictReader(
                stock_list,
                delimiter=delimiter,
            )
            for line in reader_stock_list:
                data_stock.append(line)
    else:
        with open(current_path_stock, "w", newline="") as stock_list:
            fieldnames = [
                "id",
                "product_name",
                "buy_date",
                "buy_price",
                "expiration_data",
            ]
            writer_stock_list = csv.DictWriter(
                stock_list, delimiter=delimiter, fieldnames=fieldnames
            )
            writer_stock_list.writeheader()
            for line in data:
                writer_stock_list.writerow(line)
