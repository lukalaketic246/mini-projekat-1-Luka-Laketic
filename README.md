# Mini projekat 1 - Refaktoring obrade rezervacija

## Opis
Projekat refaktorise primjer monolitne obrade rezervacija sa predavanja.
CSV red ima format `ime,broj_nocenja,cijena_po_nocenju`.

## Organizacija
- `CSV_IzvorRezervacija` ucitava CSV podatke.
- `TekstualniIzvjestavac` cuva izvjestaj.
- `izracunaj_iznos` racuna cijenu jedne rezervacije.
- `ObradaRezervacija` povezuje komponente.
- `IzvorRezervacija` i `Izvjestavac` su Protocol interfejsi.

Odgovornosti su razdvojene (S princip), a servis zavisi od Protocol interfejsa,
ne od konkretnih klasa (D princip).

## Pokretanje
```bash
uv sync
uv run python obrada.py
```

## Testiranje
```bash
uv run pytest -v
```
Testovi koriste lazni izvor i lazni izvjestavac.

## AI upotreba

### Prompt za analizu
"Postupi kao softverski arhitekta. Analiziraj dati Python kod za obradu
rezervacija i identifikuj povrede SOLID principa, posebno S i D. Navedi
konkretne probleme, posljedice i jednostavan refaktoring. Predlozi najmanje
tri pytest testa. Nemoj uvoditi nepotrebne apstrakcije."

### Prompt za refaktoring
"Refaktorisi primjer obrade rezervacija u Pythonu. Odvoji ucitavanje,
racunanje i izvjestavanje. Definisi Protocol za izvor podataka i Protocol za
izvjestavanje. Napravi servis koji prima zavisnosti kroz konstruktor. Dodaj
najmanje tri pytest testa sa laznih izvorom i izvjestavacem. Koristi tipove
i jednostavan kod."

### Korekcije
- Direktni `open()` pozivi zamijenjeni su `with` blokovima.
- Putanje fajlova se prosledjuju kroz konstruktor.
- Ucitavanje, racunanje i izvjestavanje su razdvojeni.
- Dodate su provjere neispravnih podataka.
- Testovi koriste lazne zavisnosti, bez stvarnog fajla izvjestaja.
