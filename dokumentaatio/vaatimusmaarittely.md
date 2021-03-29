# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on reseptikirjan luominen ja ylläpito.

## Käyttäjät

Ainakin aluksi sovelluksessa on ainoastaan yhden tyyppisiä käyttäjiä, eli ns. _normaaleja käyttäjiä_. Myöhemmin voidaan ehkä lisätä sovellukseen jonkinlainen ylläpidosta vastaava käyttäjärooli.  

## Käyttöliittymäluonnos
![](/kuvat/kayttoliittymaluonnos.png)

## Sovelluksen toiminnallisuudet

### Perustason toiminnallisuudet

#### Ennen kirjautumista
* Uuden käyttäjätunnuksen luominen sovellukseen
  * Käyttäjätunnuksen on oltava uniikki, muuten annetaan virheilmoitus
* Sovellukseen voi kirjautua em. tunnuksella
  * Jos tunnusta ei löydy sovelluksen tiedoista, annetaan virheilmoituksen

#### Kirjautumisen jälkeen
* Käyttäjä näkee luomansa reseptit
  * Reseptit näkyvät ainoastaan ne luoneelle käyttäjälle
* Käyttäjä voi luoda uuden reseptin
* Käyttäjä voi kirjautua ulos sovelluksesta

### Toiminnallisuuden jatkokehitys
Mahdollisuuksien mukaan sovellusta parannetaan esim. seuraavin toiminnallisuuksin:

#### Ennen kirjautumista
* Käyttäjän tulee luoda salasana uuden käyttäjätunnuksen luomisen yhteydessä
* Salasanaa kysytään kirjautuessa
  * Väärä tai puuttuva salasana aiheuttaa virheilmoituksen

#### Kirjautumisen jälkeen
* Reseptien muokkaus
* Reseptien poisto
* Käyttäjä pystyy luomaan eri kategorioita, esim. jälkiruoka, vegaani, pääsiäinen, tms. joihin reseptit voi luokitella 
* Reseptien haku eri hakuperusteilla:
  * Nimi
  * Raaka-aine
  * Em. kategoria
* Kuvien lisääminen resepteihin
* Käyttäjä voi merkitä muistiin, mitä reseptejä on kokeillut ja tarkastella niitä myöhemmin
* Käyttäjä voi jakaa luomiaan reseptejä muille käyttäjille
* Ravintoaine- ja kalorilaskuri
* Reseptin ainesosien määrien säätäminen annoksien mukaan
* Käyttäjätunnusta tai salasanaa voi muuttaa
* Käyttäjätunnuksen voi poistaa
* Sisarsovellus: Ruokakaappisovellus, jonka voi linkittää tämän yhteyteen, ja sen perusteella käyttäjälle voidaan suositella reseptejä, joihin on raaka-aineet valmiina, tai sen perusteella minkä raaka-aineen käyttö on kiireellistä, yms.
