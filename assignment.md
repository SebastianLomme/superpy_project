# Assignment Superpy 

1. Csv bestanden import

2. Een lijst van alle producten die de supermarkt heeft gekocht

3. Een vooraad lijst van alle producten
    1. Alle gekochte producten worden toegevoegd aan de voorraad lijst van alle producten
    2. Alle verkochte producten worden verwijderd van de voorraad lijst van alle producten
    3. Alle producten die over de datum gaan worden verwijderd van de voorraad lijst van alle producten

4. De tijd kan aangepast worden door het voeren van een command

5. De revenue word bijgehouden in een bestand.
    1. De revenue is per datum op de vragen
    2. De revenue is voor de hele maand op te vragen

6. De profit wordt bijgehouden in een bestanden
    1. De profit is per datum op de vragen
    2. De profit is voor de hele maand op te vragen
7. Producten die niet op voorraad zijn kunnen nier worden verkocht

8. Data structuur:
    1. alle data die binnen komt wordt opgeslagen in bought
    2. alles wat in bought staat wordt doorgezet naar inventory
        1. tenzij het product in sold staat
        2. of dat de Expiration_date is verlopen
    3. alles wat in sold staat wordt de revenue bepaald


9. Extra opdracht automatisch aanvullen van de voorraad


```python
def test():
    print("test")
```

Use `git status` to list all new or modified files that haven't yet been committed.
```bash
python main.py -h
```

```bash
python main.py report -h
```

```bash
python main.py report inventory
```

```bash
python main.py report inventory --export inventory
```

```bash
python main.py report inventory --now --export inventory
```

```bash
python main.py report inventory --yesterday --export inventory
```

```bash
python main.py report inventory --date 2021-11-20 --export inventory
```

```bash
python main.py report revenue --export revenue
```

```bash
python main.py report profit --export profit
```

```bash
python main.py report expired --export expired
```

```bash
python main.py -t
```
```bash
python main.py --today
```

```bash
python main.py -a 7
```

```bash
python main.py --advance-time 7
```

```bash
python main.py buy --product_name Salede --buy_date 2021-11-22 --buy_price 2.50 --expiration_date 2021-11-27
```


