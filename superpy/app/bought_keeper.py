import csv
from datetime import datetime
from helper import get_id, date_stamp


class Bought_keeper:
    def __init__(self, path: str) -> None:
        self.path = path
        self.fieldnames = [
            "id",
            "product_name",
            "buy_date",
            "buy_price",
            "expiration_date",
        ]

    def write_bought_file(self) -> None:
        with open(self.path, "w", newline="") as bought_file:
            writer = csv.DictWriter(
                bought_file, delimiter=";", fieldnames=self.fieldnames
            )
            writer.writeheader()

    def read_bought_to_data(self) -> list:
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

    def buy_product(
        self,
        product_name: str,
        buy_date: datetime.date,
        buy_price: float,
        expiration_date: datetime.date,
        data: list,
    ) -> None:
        product = self.make_product(product_name, buy_date, buy_price, expiration_date, data)
        with open(self.path, "a") as bought_list:
            writer = csv.DictWriter(
                bought_list, delimiter=";", fieldnames=self.fieldnames
            )
            writer.writerow(product)
        return None

    def make_product(
        self,
        product_name: str,
        buy_date: datetime.date,
        buy_price: float,
        expiration_date: datetime.date,
        data: list,
    ) -> dict:
        try:
            return {
                "id": get_id(data),
                "product_name": product_name,
                "buy_date": buy_date,
                "buy_price": buy_price,
                "expiration_date": expiration_date,
            }
        except TypeError:
            raise TypeError

    def import_bought_products(self, path: str) -> None:
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
            raise FileNotFoundError("File not found!!! check your file")
