from datetime import timedelta, datetime
from rich.table import Table
from helper import date_stamp
from variable import console


class Revenue_keeper:
    def __init__(self, data):
        self.data = data

    def get_revenue_day(self, date):
        revenue = 0
        for row in self.data:
            if date_stamp(row["sell_date"]) == date:
                revenue += row["sell_price"]
        return {"Date": date.strftime("%Y-%m-%d"), "Revenue": revenue}

    def get_revenue(self, date, to_date=""):
        date = date_stamp(date)
        to_date = date if to_date == "" else date_stamp(to_date)
        data = []
        while date <= to_date:
            data.append(self.get_revenue_day(date))
            date = date + timedelta(days=1)
        return data

    def print_revenue(self, data):
        table = Table(title="Revenue report")
        table.add_column("Date")
        table.add_column("Total revenue per day")
        for row in data:
            table.add_row(row["Date"], str(row["Revenue"]))
        table.add_row("total revenue: ", str(sum(row["Revenue"] for row in data)))
        console.print(table)
