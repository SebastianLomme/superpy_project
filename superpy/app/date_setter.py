from datetime import date, datetime, timedelta
from helper import date_stamp


class Date_setter:
    def __init__(self, path):
        self.path = path
        self.today = ""

    def set_date_today(self):
        today = date.today().strftime("%Y-%m-%d")
        self.write_date_to_file(today)
        return today

    def set_new_date_whit_days_input(self, number_days):
        today = self.read_date_from_file()
        new_date = date_stamp(today) + timedelta(days=number_days)
        new_date_string = new_date.strftime("%Y-%m-%d")
        self.write_date_to_file(new_date_string)
        return new_date_string

    def read_date_from_file(self):
        with open(self.path, "r") as today_file:
            return today_file.read()

    def write_date_to_file(self, date_string):
        with open(self.path, "w") as today_file:
            today_file.write(date_string)


    def set_date_args(self, args):
        if args.today == True:
            self.today = self.set_date_today()
            print(f"""Ok\ndate set to {self.today}""")
        elif args.days != None:
            self.today = self.set_new_date_whit_days_input(args.days)
            print(f"""Ok\ndate set to {self.today}""")
        else:
            self.today = self.read_date_from_file()
        return self.today

    # def __str__(self):
    #     return self.today
