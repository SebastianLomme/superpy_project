## Simple setup for Superpy

I wanted to make it possible to run the program with superpy instead of python app/main.py.
To make this possible I have added a setup.py. 
This allows you to install the program with a simple command
all requirements are then added to the program during installation


```python
from setuptools import setup, find_packages

setup(
    name="superpy",
    version="0.0.1",
    packages=find_packages(where="src", exclude=("tests",)),
    entry_points={"console_scripts": ["superpy=app.main:main"]},
    install_requires=["rich"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
```

## Log of all bought and sold products


I wish it could possibly keep all logs even though you might adjust the today in the program.
I solved this by rebuilding all the data each time. The bought and sold are never changed. Nothing is ever removed from these files, only something is added to them

example bought file
```python
    def read_bought_to_data(self) -> list:
        data = []
        with open(self.path, "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=";", fieldnames=self.fieldnames)
            next(reader)
            for row in reader:
                id = int(row["id"])
                product_name = str(row["product_name"])
                buy_date = date_stamp(row["buy_date"])
                buy_price = float(row["buy_price"])
                expiration_date = date_stamp(row["expiration_date"])
                data.append(
                    {
                        "id": id,
                        "product_name": product_name,
                        "buy_date": buy_date,
                        "buy_price": buy_price,
                        "expiration_date": expiration_date,
                    }
                )
            return data
```


I wanted to make it possible to test writing to and from the csv as well..
I made this possible by using fixture within pytest
These are built up for each test and broken down again after each test


```python
@pytest.fixture
def write_bought_file() -> None:
    shutil.copyfile(current_path_test, current_path_test_copy)
    yield
    print("tear_down")
    os.remove(current_path_test_copy)


@pytest.fixture
def tear_down_bought_file():
    yield
    os.remove(current_path_bought)
```

