from app.main import add


# def test_set_date_today():
#     date = Date_setter("today.txt", args).set_date_today()
#     assert date == "2021-11-24"


def test_add():
    assert add(1, 2) == 3
    
print(add(1, 2))
