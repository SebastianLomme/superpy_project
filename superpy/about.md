# Superpy CLI program

## for setup download files and then run following commands
```bash
cd superpy
python -m venv env
source env/bin/activate
pip install -e .
pip install rich
```

$~$

## Help text
```bash
python app/main.py -h
```

$~$

### Help text for sub-commands [report, buy, sell, import]
```bash
python app/app/main.py report -h
python app/app/main.py buy -h
python app/app/main.py sell -h
python app/app/main.py import -h
```

$~$

### Advanse time of program to today
```bash
python app/main.py -t
python app/main.py --today
```

### Advanse time of program whit given number of days

```bash
python app/main.py -a 7
python app/main.py --advance-time 7
```

$~$

### Print report to terminal [inventory, bought, sold, revenue, profit, expired] (default date = today)
```bash
python app/main.py report inventory
python app/main.py report bought
python app/main.py report sold
python app/main.py report revenue
python app/main.py report profit
python app/main.py report expired
```

$~$

### Date for report
[inventory, bought, sold, revenue, profit, expired]
[--now, --yesterday, --date YYYY-MM-DD]
```bash
python app/main.py report inventory --now
python app/main.py report inventory --yesterday
python app/main.py report inventory --date 2021-11-20
```

$~$

### Range of date for report
[revenue, profit]
from [--now, --yesterday, --date YYYY-MM-DD]
to [--to-now, --to-yesterday, --to-date YYYY-MM-DD]
```bash
python app/main.py report profit --date 2021-11-20 --to-now
python app/main.py report revenue --now --to-date 2021-11-30
python app/main.py report profit --yesterday --to-now
```

$~$

### Export csv file report to path dat is given (default date = today)
[inventory, bought, sold, revenue, profit, expired] 
```bash
python app/main.py report inventory --export path
python app/main.py report bought --export path
python app/main.py report sold --export path
python app/main.py report revenue --export path
python app/main.py report profit --export path
python app/main.py report expired --export path
```

$~$

### buy product 
all flags are required, date format is YYYY-MM-DD
```bash
python app/main.py buy --product-name Salade --buy-date 2021-11-22 --buy-price 2.50 --expiration-date 2021-11-27
```

$~$

### Sell product
you can only sell product that are in stock, or you will get a out of stock error!


sell-date is set to program date
```bash
python app/main.py sell --product-name Salade --sell-price 2.50
```

