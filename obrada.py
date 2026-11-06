"""Refaktorisana obrada rezervacija."""

import csv
from pathlib import Path
from typing import Protocol


class IzvorRezervacija(Protocol):
    def ucitaj(self) -> list[list[str]]: ...


class Izvjestavac(Protocol):
    def sacuvaj(self, iznosi: list[float]) -> None: ...


class CSV_IzvorRezervacija:
    def __init__(self, putanja: Path) -> None:
        self.putanja = putanja

    def ucitaj(self) -> list[list[str]]:
        with self.putanja.open("r", encoding="utf-8", newline="") as fajl:
            return list(csv.reader(fajl))


class TekstualniIzvjestavac:
    def __init__(self, putanja: Path) -> None:
        self.putanja = putanja

    def sacuvaj(self, iznosi: list[float]) -> None:
        with self.putanja.open("w", encoding="utf-8") as fajl:
            fajl.write("Iznosi rezervacija:\n")
            for iznos in iznosi:
                fajl.write(f"{iznos:.2f}\n")
            fajl.write(f"Ukupno: {sum(iznosi):.2f}\n")


def izracunaj_iznos(rezervacija: list[str]) -> float:
    if len(rezervacija) < 3:
        raise ValueError("Rezervacija mora imati najmanje 3 polja.")
    try:
        return int(rezervacija[1]) * float(rezervacija[2])
    except ValueError as greska:
        raise ValueError("Broj nocenja i cijena moraju biti brojevi.") from greska


class ObradaRezervacija:
    def __init__(self, izvor: IzvorRezervacija, izvjestavac: Izvjestavac) -> None:
        self.izvor = izvor
        self.izvjestavac = izvjestavac

    def obradi(self) -> list[float]:
        iznosi = [izracunaj_iznos(r) for r in self.izvor.ucitaj()]
        self.izvjestavac.sacuvaj(iznosi)
        return iznosi


if __name__ == "__main__":
    folder = Path(__file__).parent
    servis = ObradaRezervacija(
        CSV_IzvorRezervacija(folder / "rezervacije.csv"),
        TekstualniIzvjestavac(folder / "izvjestaj.txt"),
    )
    rezultat = servis.obradi()
    print("Poslato:", sum(rezultat))
