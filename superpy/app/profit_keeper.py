from datetime import timedelta, datetime
from rich.table import Table
from rich.console import Console
from helper import date_stamp


class Profit_keeper:
    def get_profit(self, bought_data, sold_data, inventory_data, date, to_date):
        date = date_stamp(date)
        to_date = date if to_date == "" else date_stamp(to_date)
        data_sold = []
        data_bought = []
        data = []
        total_bought = 0
        while date <= to_date:
            total_sold = 0
            for row in sold_data:
                if date_stamp(row["sell_date"]) == date:
                    total_sold += row["sell_price"]
            data_sold.append({"Date": date.strftime("%Y-%m-%d"), "Profit": total_sold})
            date = date + timedelta(days=1)
        for row in bought_data:
            print("row: ", row)
            if row["buy_date"] < date:
                total_bought += row["buy_price"]
        data_bought.append({"Date": date.strftime("%Y-%m-%d"), "buy price:": total_bought})
        print("data_bought: ", data_bought)
        return data

    def print_profit(self, data):
        table = Table(title="Profit report")
        table.add_column("Date")
        table.add_column("Total profit per day")
        for row in data:
            table.add_row(row["Date"], str(row["Profit"]))
        console = Console()
        console.print(table)

