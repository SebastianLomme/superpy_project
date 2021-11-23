from datetime import timedelta, datetime
class Revenue_keeper:
    def __init__(self, data):
        self.data = data

    def get_revenue(self, date, to_date = ""):
        date = datetime.strptime(date,"%Y-%m-%d").date()
        if to_date == "":
            to_date = date
        else:
            to_date = datetime.strptime(to_date,"%Y-%m-%d").date()
        # print("type date: ", type(date))
        # print("revenue_data: ", self.data)
        print("date, to_date", date, to_date)
        data = []
        first_date = False
        while date != to_date or first_date == False:
            total_revenue = 0
            first_date = True
            for row in self.data:
                if datetime.strptime(row["sell_date"],"%Y-%m-%d").date() == date:
                    total_revenue += row["sell_price"]
            data.append(total_revenue)
            date = date + timedelta(days=1)
            print(date)
        return data

