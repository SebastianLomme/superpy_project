from datetime import timedelta
from rich.table import Table
from app.helper import date_stamp
from rich.console import Console
import matplotlib.pyplot as plt

console = Console()


class Profit_keeper:
    def get_profit(self, bought_data, sold_data, date):

        filter_bought_data = [
            product for product in bought_data if product["buy_date"] == date
        ]
        filter_sold_data = [
            product for product in sold_data if date_stamp(product["sell_date"]) == date
        ]

        total_bought = sum(row["buy_price"] for row in filter_bought_data)
        total_sold = sum(row["sell_price"] for row in filter_sold_data)

        profit = total_sold - total_bought
        return {"Date": date.strftime("%Y-%m-%d"), "Profit": profit}

    def get_profit_data(
        self,
        bought_data,
        sold_data,
        date,
        to_date,
    ):
        date = date_stamp(date)
        to_date = date if to_date == "" else date_stamp(to_date)
        data = []
        while date <= to_date:
            data.append(self.get_profit(bought_data, sold_data, date))
            date = date + timedelta(days=1)
        return data

    def print_profit(self, data):
        table = Table(title="Profit report")
        table.add_column("Date")
        table.add_column("Total profit per day")
        for row in data:
            table.add_row(row["Date"], str(row["Profit"]))
        table.add_row("total profit: ", str(sum(row["Profit"] for row in data)))
        console.print(table)

    def print_profit_bar_chart(self, data):
        dates = []
        profit_per_date = []
        for row in data:
            dates.append(row["Date"])
            profit_per_date.append(row["Profit"])
        plt.bar(dates, profit_per_date)
        plt.title(f"Profit from {dates[0]} till {dates[-1]}" , loc="center")
        plt.tight_layout()
        plt.show()