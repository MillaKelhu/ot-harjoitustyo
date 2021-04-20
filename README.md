#  Reseptikirja-app

Sovelluksen avulla on mahdollista pitää kirjaa omista resepteistä, ja sovelluksessa voi olla useampi kirjautunut käyttäjä. Tällä hetkellä sovellukseen on mahdollista luoda uusi käyttäjä, kirjautua sillä sisään, ja kirjautua ulos.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Tarvittavat riippuvuudet asennetaan komennolla
`poetry install`

2. Alustustoimenpiteet suoritetaan komennolla
`poetry run invoke initialize-database`

3. Sovellus käynnistetään komennolla
`poetry run invoke start`
