# Testovanie – Task Manager

## Funkcia: `hlavne_menu()`

### Test Case 1 – Zobrazenie hlavného menu
- **Popis:** Overenie, že funkcia `hlavne_menu()` zobrazí všetky voľby.
- **Vstupné podmienky:** Program je spustený.
- **Kroky testu:**
  1. Spusťte program.
  2. Sledujte výpis v konzole.
- **Očakávaný výsledok:** Menu obsahuje všetky voľby (1 až 4).
- **Skutočný výsledok:** Menu sa zobrazilo správne.
- **Stav:** ✅ Pass
- **Poznámky:** Kľúčová funkcia pre navigáciu používateľa.

### Test Case 2 – Neplatná voľba v menu (negatívny test)
- **Popis:** Overenie reakcie na neplatný vstup.
- **Vstupné podmienky:** Program čaká na zadanie voľby.
- **Kroky testu:**
  1. Zadajte písmeno alebo číslo mimo rozsah (napr. "x", "9").
- **Očakávaný výsledok:** Zobrazí sa hláška „Neplatná voľba“.
- **Skutočný výsledok:** Hláška sa zobrazila.
- **Stav:** ✅ Pass
- **Poznámky:** Dôležité pre odolnosť vstupu.

---

## Funkcia: `pridat_ulohu()`

### Test Case 3 – Pridanie platnej úlohy
- **Popis:** Overenie, že úloha s názvom a popisom sa uloží.
- **Vstupné podmienky:** Zoznam úloh je prázdny.
- **Kroky testu:**
  1. Zvoľ "1".
  2. Zadajte názov: "Umyť auto"
  3. Zadajte popis: "Použiť čistú vodu a špongiu"
- **Očakávaný výsledok:** Úloha sa pridá do zoznamu.
- **Skutočný výsledok:** Úloha bola pridaná.
- **Stav:** ✅ Pass

### Test Case 4 – Prázdny názov úlohy (negatívny test)
- **Popis:** Overenie, že prázdny názov nie je akceptovaný.
- **Vstupné podmienky:** Program je v stave pridávania úlohy.
- **Kroky testu:**
  1. Zvoľ "1".
  2. Stlač Enter bez zadania názvu.
  3. Zadaj ľubovoľný popis.
- **Očakávaný výsledok:** Program upozorní a úloha sa nepridá.
- **Skutočný výsledok:** Úloha sa pridala s prázdnym názvom.
- **Stav:** ❌ Fail
- **Poznámky:** Odporúča sa doplniť validáciu.

---

## Funkcia: `zobrazit_ulohy()`

### Test Case 5 – Zobrazenie všetkých úloh
- **Popis:** Overenie, že sa vypíšu všetky úlohy v zozname.
- **Vstupné podmienky:** Zoznam obsahuje aspoň 2 úlohy.
- **Kroky testu:**
  1. Zvoľ "2".
- **Očakávaný výsledok:** Zobrazí sa číslovaný zoznam úloh.
- **Skutočný výsledok:** Zoznam sa vypísal.
- **Stav:** ✅ Pass

### Test Case 6 – Zobrazenie prázdneho zoznamu (hraničný test)
- **Popis:** Overenie, že pri prázdnom zozname sa zobrazí hláška.
- **Vstupné podmienky:** Zoznam `ulohy` je prázdny.
- **Kroky testu:**
  1. Zvoľ "2".
- **Očakávaný výsledok:** Zobrazí sa "Zoznam úloh je prázdny."
- **Skutočný výsledok:** Hláška sa zobrazila.
- **Stav:** ✅ Pass

---

## Funkcia: `odstranit_ulohu()`

### Test Case 7 – Odstránenie existujúcej úlohy
- **Popis:** Overenie, že úloha sa odstráni podľa čísla.
- **Vstupné podmienky:** Zoznam obsahuje aspoň 1 úlohu.
- **Kroky testu:**
  1. Zvoľ "3".
  2. Zadaj "1".
- **Očakávaný výsledok:** Úloha sa odstráni, zobrazí sa potvrdenie.
- **Skutočný výsledok:** Úloha bola odstránená.
- **Stav:** ✅ Pass

### Test Case 8 – Zadanie neexistujúceho čísla (negatívny test)
- **Popis:** Overenie reakcie na číslo mimo rozsah.
- **Vstupné podmienky:** Zoznam obsahuje napr. 2 úlohy.
- **Kroky testu:**
  1. Zvoľ "3".
  2. Zadaj "5".
- **Očakávaný výsledok:** Zobrazí sa chyba.
- **Skutočný výsledok:** Hláška sa zobrazila.
- **Stav:** ✅ Pass

### Test Case 9 – Odstránenie poslednej úlohy (hraničný test)
- **Popis:** Overenie, že je možné odstrániť poslednú úlohu.
- **Vstupné podmienky:** Zoznam obsahuje presne 1 úlohu.
- **Kroky testu:**
  1. Zvoľ "3".
  2. Zadaj "1".
- **Očakávaný výsledok:** Úloha sa odstráni, zoznam bude prázdny.
- **Skutočný výsledok:** Prebehlo správne.
- **Stav:** ✅ Pass
