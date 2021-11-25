from datetime import timedelta, datetime
from rich.table import Table
from rich.console import Console
from helper import date_stamp


class Revenue_keeper:
    def __init__(self, data):
        self.data = data

    def get_revenue(self, date, to_date):
        date = date_stamp(date)
        to_date = date if to_date == "" else date_stamp(to_date)
        data = []
        while date <= to_date:
            total_revenue = 0
            for row in self.data:
                if date_stamp(row["sell_date"]) == date:
                    total_revenue += row["sell_price"]
            data.append({"Date": date.strftime("%Y-%m-%d"), "Revenue": total_revenue})
            date = date + timedelta(days=1)
        return data

    def print_revenue(self, data):
        table = Table(title="Revenue report")
        table.add_column("Date")
        table.add_column("Total revenue per day")
        for row in data:
            table.add_row(row["Date"], str(row["Revenue"]))
        console = Console()
        console.print(table)
        pass
