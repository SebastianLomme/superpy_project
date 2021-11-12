# Imports
import csv
from datetime import date, timedelta, datetime
import os
from create_files import (
    read_bought_to_data,
    read_sold_list,
    reader_stock_list,
    current_path_sold,
    current_path_bought,
    data_sold,
    data,
    data_stock,
    current_path_today,
    delimiter,
)
from parser import args


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# current_path_bought = os.path.join(os.path.dirname(__file__), 'bought.csv')


# Your code below this line.


def set_date_today():
    with open(current_path_today, "w") as today_file:
        today = date.today().strftime("%d/%m/%Y")
        today_file.write(today)
    return today


if os.path.exists(current_path_today):
    pass
else:
    today = set_date_today()


def set_date(number_days):
    with open(current_path_today, "r") as today_file:
        today = today_file.read()
    new_date = datetime.strptime(today, "%d/%m/%Y") + timedelta(days=number_days)
    new_date_string = new_date.strftime("%d/%m/%Y")
    with open(current_path_today, "w") as today_file:
        today_file.write(new_date_string)
    return new_date_string


def set_new_date_today(args):
    global today
    if args.today == True:
        today = set_date_today()
        print("Ok")
    elif args.days != None:
        today = set_date(args.days)
        print("Ok")
    else:
        with open(current_path_today, "r") as today_file:
            today = today_file.read()


def set_delimiter():
    global delimiter
    if args.delimiter == "comma":
        delimiter = ","
    elif args.delimiter == "semicolon":
        delimiter = ";"
    elif args.delimiter == "tab":
        delimiter = "\t"
    elif args.delimiter == "space":
        delimiter = " "
    elif args.delimiter == "pipe":
        delimiter = "|"


def sell_product(
    bought_id,
    sell_price,
):
    sell_product = {
        "id": get_id(data_sold),
        "bought_id": int(bought_id),
        "sell_date": today,
        "sell_price": sell_price,
    }
    fieldnames = ["id", "bought_id", "sell_date", "sell_price"]
    with open(current_path_sold, "a") as sold_list:
        writer = csv.DictWriter(sold_list, delimiter=delimiter, fieldnames=fieldnames)
        writer.writerow(sell_product)
    return sell_product


def buy_product(product_name, buy_date, buy_price, expiration_data):
    buy_product = {
        "id": get_id(data),
        "product_name": product_name,
        "buy_date": buy_date,
        "buy_price": buy_price,
        "expiration_data": expiration_data,
    }
    fieldnames = ["id", "product_name", "buy_date", "buy_price", "expiration_data"]
    with open(current_path_bought, "a") as bought_list:
        writer = csv.DictWriter(bought_list, delimiter=delimiter, fieldnames=fieldnames)
        writer.writerow(buy_product)
    return buy_product


def get_stock():
    for product in data:
        if str(product["id"]) not in [product["bought_id"] for product in data_sold]:
            print("Today: ", datetime.strptime(today, "%d/%m/%Y"))
            if product["expiration_data"] > datetime.strptime(today, "%d/%m/%Y"):
                print("test")
                data_stock.append(product)
            print("Expiration: ", product["expiration_data"])
            # print("test", [d['id'] for d in data_sold])


def get_id(list_data):
    if len(list_data) == 0:
        return 1
    else:
        return int(list_data[-1]["id"]) + 1


def main():
    read_bought_to_data()
    read_sold_list()
    reader_stock_list
    set_new_date_today(args)
    set_delimiter()
    if args.command == "sell":
        sell_product(args.id, args.sell_price)
        read_sold_list()
    elif args.command == "buy":
        buy_product(
            args.product_name, args.buy_date, args.buy_price, args.expiration_date
        )
        read_bought_to_data()
    get_stock()
    for line in data_stock:
        print("Data_stock: ", line)
    print("today:", today)


if __name__ == "__main__":
    main()
