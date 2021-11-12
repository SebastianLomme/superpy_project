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