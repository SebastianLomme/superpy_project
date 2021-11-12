import os
import csv
from datetime import date, timedelta, datetime
from helper import get_id

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
            for row in read_sold_list:
                id = int(row["id"])
                bought_id = int(row["bought_id"])
                sell_date = row["sell_date"]
                sell_price = float(row["sell_price"])
                data_sold.append({
                    "id": id,
                    "bought_id": bought_id,
                    "sell_date": sell_date,
                    "sell_price": sell_price
                })
    else:
        with open(current_path_sold, "w", newline="") as sold_list:

            fieldnames = ["id", "bought_id", "sell_date", "sell_price"]
            writer_sold_list = csv.DictWriter(
                sold_list, delimiter=delimiter, fieldnames=fieldnames
            )
            writer_sold_list.writeheader()
            for row in data_sold:
                writer_sold_list.write(row)


def writer_stock_list():
    with open(current_path_stock, "w", newline="") as stock_list:
            fieldnames = [
                "id",
                "bought_id",
                "product_name",
                "number_in_stock"
            ]
            writer_stock_list = csv.DictWriter(
                stock_list, delimiter=delimiter, fieldnames=fieldnames
            )
            writer_stock_list.writeheader()
            total_list_stock = []
            for row in data_stock:
                # product = {}
                if row["product_name"] in [product["product_name"] for product in total_list_stock]:
                    print(row["product_name"])
                    for product in total_list_stock:
                        if product["product_name"] == row["product_name"]:
                            print("test", product)
                            product["bought_id"].append(row["id"])
                            product["number_in_stock"] = len(product["bought_id"])
                else:
                    bought_id = [row["bought_id"]]
                    product = {
                        "id": get_id(total_list_stock),
                        "bought_id": bought_id,
                        "product_name": row["product_name"],
                        "number_in_stock": len(bought_id)
                    }
                    total_list_stock.append(product)
            for row in total_list_stock:
                writer_stock_list.writerow(row)

