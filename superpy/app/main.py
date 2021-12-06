# Imports
from app.parsers import args
from app.setup_keeper import Setup_keeper
from app.helper import args_date
from app.revenue_keeper import Revenue_keeper
from app.profit_keeper import Profit_keeper
from app.date_setter import Date_setter
from app.variable import (
    bought_keeper,
    sold_keeper,
    inventory_keeper,
    current_path_today,
)

from datetime import datetime, timedelta


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def command_sell(today, yesterday):
    # addeds a sold product to the logs

    data_bought = bought_keeper.read_bought_to_data()
    data_sold = sold_keeper.read_sold_list()
    data_stock = inventory_keeper.get_stock(today, data_bought, data_sold)
    sold_keeper.sell_product(
        args.product_name, args.sell_price, today, data_sold, data_stock
    )
    data_sold = sold_keeper.read_sold_list()


def command_buy(today, yesterday):
    # addeds a bought product to the log

    data_bought = bought_keeper.read_bought_to_data()
    bought_keeper.buy_product(
        args.product_name,
        args.buy_date,
        args.buy_price,
        args.expiration_date,
        data_bought,
    )


def command_report(today, yesterday):
    # function for choosing the different reports via the given args

    data_bought = bought_keeper.read_bought_to_data()
    data_sold = sold_keeper.read_sold_list()


    date = args_date(args.report_date, today, yesterday)
    to_date = args_date(args.report_to_date, today, yesterday)


    if args.report == "inventory":
        inventory_data = inventory_keeper.make_report_stock(
            date, data_bought, data_sold
        )
        if args.report_export != None:
            inventory_keeper.export_report_csv(
                inventory_data, f"{args.report_export}_{date}.csv"
            )
    elif args.report == "revenue":
        revenue = Revenue_keeper(data_sold).get_revenue(date, to_date)
        Revenue_keeper(data_sold).print_revenue(revenue)
        Revenue_keeper(data_sold).print_revenue_bar_chart(revenue)
        if args.report_export != None:
            inventory_keeper.export_report_csv(
                revenue, f"{args.report_export}_{date}.csv"
            )
    elif args.report == "profit":
        profit_data = Profit_keeper().get_profit_data(
            data_bought, data_sold, date, to_date
        )
        Profit_keeper().print_profit(profit_data)
        Profit_keeper().print_profit_bar_chart(profit_data)
        if args.report_export != None:
            inventory_keeper.export_report_csv(
                profit_data, f"{args.report_export}_{date}.csv"
            )
    elif args.report == "expired":
        expired_data = inventory_keeper.make_report_expired(
            date, data_bought, data_sold
        )
        if args.report_export != None:
            inventory_keeper.export_report_csv(
                expired_data, f"{args.report_export}_{date}.csv"
            )

    elif args.report == "bought":
        bought_data = bought_keeper.make_report_bought_products(data_bought, date)
        if args.report_export != None:
            inventory_keeper.export_report_csv(
                bought_data, f"{args.report_export}_{date}.csv"
            )

    elif args.report == "sold":
        sold_data = sold_keeper.make_report_sold_products(data_sold, date)
        if args.report_export != None:
            inventory_keeper.export_report_csv(
                sold_data, f"{args.report_export}_{date}.csv"
            )


def command_import(today, yesterday):

    bought_keeper.import_bought_products(args.path)


command = {
    "buy": command_buy,
    "sell": command_sell,
    "report": command_report,
    "import": command_import,
}


def main():
    # setup_keeper makes file dir if not yet exist
    Setup_keeper().make_file_dir_if_not_exist()

    # sets date
    today = str(Date_setter(current_path_today).set_date_args(args))
    yesterday = (
        datetime.strptime(today, "%Y-%m-%d").date() - timedelta(days=1)
    ).strftime("%Y-%m-%d")

    # handels de given commands
    if args.command != None:
        command[args.command](today, yesterday)
    print(args)


if __name__ == "__main__":
    main()
