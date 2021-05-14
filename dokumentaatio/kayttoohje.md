# Käyttöohje
Lataa projektin viimeisin release [https://github.com/MillaKelhu/ot-harjoitustyo/releases/latest] valitsemalla *Assets* -osiosta *Source code*.

## Konfigurointi
Tietojen pysyväistallennukseen tarvittavan sqlite-tiedoston nimen voi halutessaan muuttaa käynnistyshakemiston _.env_-tiedostossa. Tiedosto luodaan automaattisesti _data_-kansioon, jos sitä ei ole. _.env_-tiedoston muoto on seuraava:
`database_name = database.sqlite`

## Esivaatimukset
Jotta ohjelman voi asentaa ja suorittaa, varmista, että [poetry](https://python-poetry.org/docs/#installation) on asennettu ja [python](https://www.python.org/downloads/) on vähintäänkin 3.6.

## Ohjelman asennus
Asenna ensin tarvittavat riippuvuudet komennolla 
`poetry install`

Suorita seuraavaksi tarvittavat alustustoimenpiteet komennolla
`poetry run invoke initialize-database`

Sovellus käynnistetään komennolla
`poetry run invoke start`

## Käynnistämisen jälkeen

### Kirjautuminen
Sovellus avaa aina ensin kirjautumisnäkymän.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/login_view.png)

Kirjautuminen onnistuu käyttäjänimen ja salasanan syöttämisellä syötekenttiin ja painamalla nappia "Log in".

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/login_view_input.png)

### Uuden käyttäjän luominen
Jos käyttäjäprofiilia ei ole, sen voi luoda painamalla kirjautumisnäkymän nappia "Sign in", josta avautuu seuraavanlainen näkymä: 

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/signin_view.png)

Uuden käyttäjän luominen onnistuu uuden käyttäjänimen ja salasanan syöttämisellä syötekenttiin ja painamalla nappia "Create new user". Tämän jälkeen näkymä siirtyy takaisin kirjautumiseen. Myös nappi "Cancel" siirtää näkymän kirjautumiseen, mutta ei luo uutta käyttäjää.

### Keittokirja
Onnistuneen kirjautumisen jälkeen käyttäjälle näytetään tämän oma henkilökohtainen keittokirja.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/bookview_vko7_1.png)

Reseptinappeja painamalla käyttäjä voi siirtyä tarkastelemaan luomiaan reseptejä.

## Reseptien haku
Keittokirjasta tiettyjä reseptejä haettaessa riittää, että hakusana kirjoitetaan hakusana syötekenttään, joka sijaitsee "New recipe" ja "Log out" -nappien alla, ja painetaan nappia "Search" syötekentän vieressä.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/search_2.png)

### Uuden reseptin luominen
Painamalla keittokirjanäkymän vasemmalla sijaitsevaa nappia "New recipe" siirrytään näkymään, jossa käyttäjä voi luoda uuden reseptin.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/new_recipe_view.png)

Reseptin tallentaminen ei onnistu, jos syötekentät ovat tyhjiä.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/new_recipe_aglio_e_olio.png)

Reseptin tallentaminen onnistuu vasemmasta alakulmasta painamalla nappia "Create new recipe". Reseptin tallentamisen jälkeen näkymä siirtyy takaisin keittokirjaan. Vaihtoehtoisesti Käyttäjä voi palata keittokirjanäkymään painamalla nappia "Return without saving" oikeassa alakulmassa, jolloin resepti ei tallennu.

### Reseptin tarkastelu
Keittokirjanäkymän reseptien nimet sisältäviä nappeja painamalla käyttäjä pääsee tarkastelemaan reseptejä tarkemmin.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/view_recipe_boba.png)

Vasemman alakulman nappi "Return" palauttaa näkymän takaisin keittokirjaan. Keskellä alhaalla oleva nappi "Modify recipe" avaa näkymän, jossa reseptin sisältöä voi muokata. Oikean alakulman napin "Delete recipe" kautta taas resepti on mahdollista poistaa.

### Reseptin muokkaus
Painamalla em. näkymässä nappia "Modify recipe" avaa seuraavanlaisen näkymän:

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/modify_boba_1.png)

Ohjeen syötekenttä on nyt siis vapaasti muokattavissa.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/modify_boba_2.png)

Muokatun ohjeen voi tallentaa vasemmalla alakulmassa sijaitsevasta napista "Save modified recipe". Tallennuksen jälkeen näkymä siirtyy takaisin reseptinäkymään. Vaihtoehtoisesti reseptinäkymään voi palata painamalla oikeassa alakulmassa sijaitsevaa nappia "Return without saving", jolloin muokkaukset eivät tallennu.
**HUOM!** Muokkauksia ei voi peruuttaa.

### Reseptin poisto
Painamalla reseptinäkymästä nappia "Delete recipe" avautuu pienempi ikkuna, joka kysyy käyttäjän vahvistuksen reseptin poistolle.

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/delete_recipe_1.png)

Painamalla pikkuikkunan vasemmassa alakulmassa olevaa nappia "Cancel" pikkuikkuna sulkeutuu, ja jäljelle jää tavanomainen reseptinäkymä. Jos taas painetaan oikeassa alakulmassa olevaa nappia "Delete" resepti poistetaan, pikkuikkuna sulkeutuu, ja näkymä siirtyy takaisin keittokirjaan.
**HUOM!** Poistettuja reseptejä ei voi saada takaisin.
