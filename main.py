from collections import namedtuple

args_tuple = namedtuple("args", "today days")

args = args_tuple("2021-11-25", "None", None)


def check_passport(passport, country_of_destination, allowed_country, not_allowed_country):
allowed_country = {'nationality': ['country_of_destination']}
not_allowed_country = {'country_of_destination': ['forbidden_country_1', 'forbidden_country_2', 'forbidden_country_3']}
    if passport['nationality'] not in allowed_country:
        return False
    if country_of_destination not in allowed_country:
        return False
    if passport['stamps'] in not_allowed_country:
        return False 