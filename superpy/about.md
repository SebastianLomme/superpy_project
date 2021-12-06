# Superpy CLI program

## for setup download files and then run following commands
```bash
cd superpy
python -m venv env
source env/bin/activate
pip install -e .
pip install rich

pip install git+https://github.com/SebastianLomme/superpy_project.git


```

$~$

## Help text
```bash
superpy -h
```

$~$

### Help text for sub-commands [report, buy, sell, import]
```bash
superpy report -h
superpy buy -h
superpy sell -h
superpy import -h
```

$~$

### Advanse time of program to today
```bash
superpy -t
superpy --today
```

### Advanse time of program whit given number of days

```bash
superpy -a 7
superpy --advance-time 7
```

$~$

### Print report to terminal [inventory, bought, sold, revenue, profit, expired] (default date = today)
```bash
superpy report inventory
superpy report bought
superpy report sold
superpy report revenue
superpy report profit
superpy report expired
```

$~$

### Date for report
[inventory, bought, sold, revenue, profit, expired]
[--now, --yesterday, --date YYYY-MM-DD]
```bash
superpy report inventory --now
superpy report inventory --yesterday
superpy report inventory --date 2021-11-20
```

$~$

### Range of date for report
[revenue, profit]
from [--now, --yesterday, --date YYYY-MM-DD]
to [--to-now, --to-yesterday, --to-date YYYY-MM-DD]
```bash
superpy report profit --date 2021-11-20 --to-now
superpy report revenue --now --to-date 2021-11-30
superpy report profit --yesterday --to-now
```

$~$

### Export csv file report as filename dat is given (default date = today)
[inventory, bought, sold, revenue, profit, expired] 
```bash
superpy report inventory --export filename
superpy report bought --export filename
superpy report sold --export filename
superpy report revenue --export filename
superpy report profit --export filename
superpy report expired --export filename
```

$~$

### buy product 
all flags are required, date format is YYYY-MM-DD
```bash
superpy buy --product-name Salade --buy-date 2021-11-22 --buy-price 2.50 --expiration-date 2021-11-27
```

$~$

### Sell product
you can only sell product that are in stock, or you will get a out of stock error!


sell-date is set to program date
```bash
superpy sell --product-name Salade --sell-price 2.50
```

