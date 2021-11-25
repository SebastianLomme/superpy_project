import csv
from datetime import datetime
from helper import get_id, date_stamp


class Bought_keeper:
    def __init__(self, path):
        self.path = path
        self.fieldnames = [
            "id",
            "product_name",
            "buy_date",
            "buy_price",
            "expiration_date",
        ]

    def read_bought_to_data(self):
        data = []
        with open(self.path, "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=";", fieldnames=self.fieldnames)
            next(reader)
            for row in reader:
                id = int(row["id"])
                product_name = str(row["product_name"])
                buy_date = date_stamp(row["buy_date"])
                buy_price = float(row["buy_price"])
                expiration_date = date_stamp(row["expiration_date"])
                data.append(
                    {
                        "id": id,
                        "product_name": product_name,
                        "buy_date": buy_date,
                        "buy_price": buy_price,
                        "expiration_date": expiration_date,
                    }
                )
            return data

    def buy_product(self, product_name, buy_date, buy_price, expiration_date, data):
        buy_product = {
            "id": get_id(data),
            "product_name": product_name,
            "buy_date": buy_date,
            "buy_price": buy_price,
            "expiration_date": expiration_date,
        }
        with open(self.path, "a") as bought_list:
            writer = csv.DictWriter(
                bought_list, delimiter=";", fieldnames=self.fieldnames
            )
            writer.writerow(buy_product)
        return None

    def import_bought_products(self, path):
        try:
            with open(self.path, "r+") as bought_list:
                reader_bought = bought_list.readlines()
                writer = csv.DictWriter(
                    bought_list, delimiter=";", fieldnames=self.fieldnames
                )
                with open(path, "r") as imported_products:
                    reader = csv.DictReader(
                        imported_products, delimiter=";", fieldnames=self.fieldnames
                    )
                    id = reader_bought[-1].split(";")[0]
                    id = int(id)
                    next(reader)
                    for row in reader:
                        id += 1
                        row["id"] = id
                        writer.writerow(row)
        except FileNotFoundError:
            print("File not found!!! check your file")
