import csv

from rich.console import Console
from helper import get_id
from datetime import datetime
from rich.table import Table


class Inventory_keeper:
    def __init__(self, path):
        self.path = path
        self.stock_data = []

    def writer_stock_list(self, data_stock):
        with open(self.path, "w", newline="") as stock_list:
            fieldnames = [
                "id",
                "bought_id",
                "product_name",
                "buy_price",
                "expiration_date",
                "number_in_stock",
                "buy_date",
            ]
            writer_stock_list = csv.DictWriter(
                stock_list, delimiter=";", fieldnames=fieldnames
            )
            writer_stock_list.writeheader()
            total_list_stock = self.group_same_products(data_stock)
            for row in total_list_stock:
                writer_stock_list.writerow(row)


    def get_stock(self, date, data_bought, data_sold):
        data_stock = []
        filter_bought_data = [product for product in data_bought if product["buy_date"] < datetime.strptime(date, "%Y-%m-%d").date() ]
        for product in filter_bought_data:
            if product["id"] not in [product["bought_id"] for product in data_sold]:
                if (
                    product["expiration_date"]
                    >= datetime.strptime(date, "%Y-%m-%d").date()
                ):
                    data_stock.append({**product, "bought_id": product["id"]})
        self.writer_stock_list(data_stock)
        return data_stock


    def make_report_stock(self, date,  data_bought, data_sold):
        data_stock = []
        filter_bought_data = [product for product in data_bought if product["buy_date"] < datetime.strptime(date, "%Y-%m-%d").date() ]
        filter_sold_data = [product for product in data_sold if datetime.strptime(product["sell_date"], "%Y-%m-%d").date() > datetime.strptime(date, "%Y-%m-%d").date() ]
        for product in filter_bought_data:
            if product["id"] not in [product["bought_id"] for product in filter_sold_data]:
                if (
                    product["expiration_date"]
                    >= datetime.strptime(date, "%Y-%m-%d").date()
                ):
                    data_stock.append({**product, "bought_id": product["id"]})
        report_list = self.group_same_products(data_stock)
        self.print_data_stock(report_list, date)

    def make_report_expired(self, date, data_bought, data_sold):
        data_stock = []
        filter_bought_data = [product for product in data_bought if product["buy_date"] < datetime.strptime(date, "%Y-%m-%d").date() ]
        filter_sold_data = [product for product in data_sold if datetime.strptime(product["sell_date"], "%Y-%m-%d").date() > datetime.strptime(date, "%Y-%m-%d").date()]
        for product in filter_bought_data:
            if product["id"] not in [product["bought_id"] for product in filter_sold_data]:
                if (
                    product["expiration_date"]
                    < datetime.strptime(date, "%Y-%m-%d").date()
                ):
                    data_stock.append({**product, "bought_id": product["id"]})
        report_list = self.group_same_products(data_stock)
        self.print_data_expired(report_list, date)


    def print_data_stock(self, data, date):
        table = Table(title=f"Inventory list {date}")
        table.add_column("id")
        table.add_column("product_name")
        table.add_column("number_in_stock")
        table.add_column("buy_price")
        table.add_column("expiration_date")
        table.add_column("bought_id")
        for row in data:
            table.add_row(
                str(row["id"]),
                row["product_name"],
                str(row["number_in_stock"]),
                str(row["buy_price"]),
                row["expiration_date"].strftime("%Y-%m-%d"),
                str(row["bought_id"]),
            )

        console = Console()
        console.print(table)

    def print_data_expired(self, data, date):
        table = Table(title=f"Expired product list {date}")
        table.add_column("id")
        table.add_column("product_name")
        table.add_column("number_of_expired")
        table.add_column("buy_price")
        table.add_column("expiration_date")
        table.add_column("bought_id")
        for row in data:
            table.add_row(
                str(row["id"]),
                row["product_name"],
                str(row["number_in_stock"]),
                str(row["buy_price"]),
                row["expiration_date"].strftime("%Y-%m-%d"),
                str(row["bought_id"]),
            )

        console = Console()
        console.print(table)

    def group_same_products(self, data_stock):
        data = []
        for row in data_stock:
            if (row["product_name"], row["buy_price"], row["expiration_date"]) in [
                (
                    product["product_name"],
                    product["buy_price"],
                    product["expiration_date"],
                )
                for product in data
            ]:

                for product in data:

                    if (
                        product["product_name"],
                        product["buy_price"],
                        product["expiration_date"],
                    ) == (
                        row["product_name"],
                        row["buy_price"],
                        row["expiration_date"],
                    ):
                        product["bought_id"].append(row["id"])
                        product["number_in_stock"] = len(product["bought_id"])
            else:
                bought_id = [row["bought_id"]]
                product = {
                    "id": get_id(data),
                    "bought_id": bought_id,
                    "buy_price": row["buy_price"],
                    "expiration_date": row["expiration_date"],
                    "product_name": row["product_name"],
                    "number_in_stock": len(bought_id),
                }
                data.append(product)
        return data                   

  