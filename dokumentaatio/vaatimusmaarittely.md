# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on reseptikirjan luominen ja ylläpito.

## Käyttäjät

Ainakin aluksi sovelluksessa on ainoastaan yhden tyyppisiä käyttäjiä, eli ns. _normaaleja käyttäjiä_. Myöhemmin voidaan ehkä lisätä sovellukseen jonkinlainen ylläpidosta vastaava käyttäjärooli.  

## Käyttöliittymäluonnos
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/kayttoliittymaluonnos.png)

## Sovelluksen toiminnallisuudet

### Perustason toiminnallisuudet

#### Ennen kirjautumista
* Uuden käyttäjätilin luominen sovellukseen. Käyttäjätili sisältää käyttäjänimen ja salasanan.
  * Käyttäjänimen on oltava uniikki, muuten annetaan virheilmoitus.
  * Sekä käyttäjänimen että salasanan on myös oltava 1-99 merkkiä pitkä, muuten annetaan virheilmoitus.
* Sovellukseen voi kirjautua em. nimellä ja salasanalla.
  * Jos käyttäjänimi tai salasana ovat virheelliset, annetaan virheilmoitus eikä käyttäjää päästetä sisään.

#### Kirjautumisen jälkeen
* Käyttäjä näkee luomansa reseptit.
  * Reseptit näkyvät ainoastaan ne luoneelle käyttäjälle
  * Näkyviä reseptejä voi filtteröidä. Tällöin näkyvillä ovat vain ne käyttäjän reseptit, joiden nimessä tai sisällössä on käyttäjän antama hakusana.
* Käyttäjä voi luoda uuden reseptin
  * Reseptin nimen on oltava käyttäjän omien reseptien joukossa uniikki ja 1-99 merkkiä pitkä, muuten annetaan virheilmoitus.
  * Reseptin sisällön on oltava 1-5000 merkkiä pitkä, muuten annetaan virheilmoitus.
* Käyttäjä voi muokata luomiaan reseptejä.
  * Reseptin muokatun sisällön on oltava 1-5000 merkkiä pitkä, muuten annetaan virheilmoitus.
* Käyttäjä voi poistaa luomiaan reseptejä.
  * Käyttäjän on erikseen vaihvistettava poisto ikävien huolimattomuusvirheiden minimoimiseksi.
* Käyttäjä voi kirjautua ulos sovelluksesta
