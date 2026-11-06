from obrada import ObradaRezervacija, izracunaj_iznos


class LazniIzvor:
    def __init__(self, rezervacije: list[list[str]]) -> None:
        self.rezervacije = rezervacije

    def ucitaj(self) -> list[list[str]]:
        return self.rezervacije


class LazniIzvjestavac:
    def __init__(self) -> None:
        self.sacuvani_iznosi: list[float] | None = None

    def sacuvaj(self, iznosi: list[float]) -> None:
        self.sacuvani_iznosi = iznosi


def test_izracunaj_iznos() -> None:
    assert izracunaj_iznos(["Ana", "3", "25"]) == 75.0


def test_obrada_vise_rezervacija() -> None:
    izvjestavac = LazniIzvjestavac()
    servis = ObradaRezervacija(
        LazniIzvor([["Ana", "2", "30"], ["Marko", "3", "20"]]),
        izvjestavac,
    )
    assert servis.obradi() == [60.0, 60.0]
    assert izvjestavac.sacuvani_iznosi == [60.0, 60.0]


def test_obrada_prazne_liste() -> None:
    izvjestavac = LazniIzvjestavac()
    servis = ObradaRezervacija(LazniIzvor([]), izvjestavac)
    assert servis.obradi() == []
    assert izvjestavac.sacuvani_iznosi == []


def test_neispravna_rezervacija() -> None:
    try:
        izracunaj_iznos(["Ana", "dva", "25"])
    except ValueError as greska:
        assert "moraju biti brojevi" in str(greska)
    else:
        raise AssertionError("Ocekivana je ValueError greska.")
