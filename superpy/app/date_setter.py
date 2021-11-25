from datetime import date, datetime, timedelta
from app.helper import date_stamp

class Date_setter:
    def set_date_today(self):
        with open(self.path, "w") as today_file:
            today = date.today().strftime("%Y-%m-%d")
            today_file.write(today)
        return today

    def set_date(self, number_days):
        with open(self.path, "r") as today_file:
            today = today_file.read()
        new_date = date_stamp(today) + timedelta(
            days=number_days
        )
        new_date_string = new_date.strftime("%Y-%m-%d")
        with open(self.path, "w") as today_file:
            today_file.write(new_date_string)
        return new_date_string

    def __init__(self, path, args):
        self.path = path
        self.args = args
        self.today = ""
        if self.args.today == True:
            self.today = self.set_date_today()
            print(f"""Ok\ndate set to {self.today}""")
        elif args.days != None:
            self.today = self.set_date(args.days)
            print(f"""Ok\ndate set to {self.today}""")
        else:
            with open(self.path, "r") as today_file:
                self.today = today_file.read()

    def __str__(self):
        return self.today
