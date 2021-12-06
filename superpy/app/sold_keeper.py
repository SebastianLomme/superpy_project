import os
import csv
from superpy.app.helper import get_id, date_stamp
from rich.table import Table
from rich.console import Console


class Sold_keeper:
    def __init__(self, path):
        self.path = path
        self.fieldnames = ["id", "bought_id", "sell_date", "sell_price"]

    def read_sold_list(self):
        data_sold = []
        if os.path.exists(self.path):
            with open(self.path, "r", newline="") as sold_list:
                read_sold_list = csv.DictReader(
                    sold_list, delimiter=";", fieldnames=self.fieldnames
                )
                next(read_sold_list)
                for row in read_sold_list:
                    id = int(row["id"])
                    bought_id = int(row["bought_id"])
                    sell_date = row["sell_date"]
                    sell_price = float(row["sell_price"])
                    data_sold.append(
                        {
                            "id": id,
                            "bought_id": bought_id,
                            "sell_date": sell_date,
                            "sell_price": sell_price,
                        }
                    )
        else:
            with open(self.path, "w", newline="") as sold_list:

                fieldnames = ["id", "bought_id", "sell_date", "sell_price"]
                writer_sold_list = csv.DictWriter(
                    sold_list, delimiter=";", fieldnames=fieldnames
                )
                writer_sold_list.writeheader()
                for row in data_sold:
                    writer_sold_list.write(row)
        return data_sold

    def sell_product(self, product_name, sell_price, date, data_sold, data_stock):
        bought_id = ""
        for row in data_stock:
            if product_name == row["product_name"]:
                bought_id = row["bought_id"]
                print("Ok")
                break
        else:
            print("ERROR: Product not in stock")
            return None
        sell_product = {
            "id": get_id(data_sold),
            "bought_id": bought_id,
            "sell_date": date,
            "sell_price": sell_price,
        }
        with open(self.path, "a") as sold_list:
            writer = csv.DictWriter(
                sold_list, delimiter=";", fieldnames=self.fieldnames
            )
            writer.writerow(sell_product)
        return None

    def make_report_sold_products(self, data, date):
        list_report = [
            row for row in data if date_stamp(row["sell_date"]) == date_stamp(date)
        ]
        self.print_data_sold(list_report, date)
        return list_report

    def print_data_sold(self, data, date):
        table = Table(title=f"Sold products list {date}")
        table.add_column("id")
        table.add_column("bought_id")
        table.add_column("sell_date")
        table.add_column("sell_price")

        for row in data:
            table.add_row(
                str(row["id"]),
                str(row["bought_id"]),
                row["sell_date"],
                str(row["sell_price"]),
            )
        console = Console()
        console.print(table)
