# Task Manager

Správca úloh napísaný v Pythone. Umožňuje používateľovi:

- Pridávať nové úlohy
- Zobrazovať uložené úlohy
- Odstraňovať úlohy
- Ukončiť program

## Spustenie

1. Stiahni súbor `task_manager.py`.
2. Spusť v termináli alebo editore (napr. VS Code):

```bash
python task_manager.py

## Popis funkcií

- `hlavne_menu()` – zobrazuje hlavné menu a načíta voľbu od používateľa.
- `pridat_ulohu()` – umožní zadať názov a popis úlohy a uloží ju do zoznamu.
- `zobrazit_ulohy()` – zobrazí všetky úlohy, ak existujú.
- `odstranit_ulohu()` – odstráni úlohu na základe čísla zo zoznamu.

## Testovanie

Manuálne testy sa nachádzajú v súbore [`TESTY.md`](./TESTY.md).

Testované boli:

- **Pozitívne prípady** – správne použitie všetkých funkcií
- **Negatívne prípady** – napr. prázdny názov, neexistujúce číslo úlohy
- **Hraničné prípady** – prázdny zoznam, posledná úloha atď.

> V prípade zadania chybného vstupu sa zobrazí príslušná hláška. Validácia vstupov je zatiaľ len čiastočná.

## Autor

Timotej Šebest  
GitHub: [@Timotej365](https://github.com/Timotej365)
