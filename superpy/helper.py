def get_id(list_data):
    if len(list_data) == 0:
        return 1
    else:
        return int(list_data[-1]["id"]) + 1