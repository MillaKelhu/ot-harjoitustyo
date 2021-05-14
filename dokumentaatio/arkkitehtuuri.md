# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmikerroksista kerrosarkkitehtuuria, jossa ylimpänä on käyttöliittymästä vastaava kerros, pakkauskaaviossa *ui*. Seuraavana on sovelluslogiikasta vastaava kerros, pakkauskaaviossa *functions*, ja alimpana on datan tallennuksesta ja tietokannasta vastaava kerros, pakkauskaaviossa *datacontrol*. 

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/ohte_package_diagram_detail_1.png)

## Käyttöliittymä

Käyttöliittymässä on periaatteessa seitsemän erilaista näkymää. Seuraavista kuudesta näkymästä voi näkyä vain yksi kerrallaan:

* Kirjautuminen
* Uuden käyttäjätilin luominen
* Reseptikirja
* Uuden reseptin luominen
* Reseptin tarkastelu
* Reseptin muokkaus

Ja lisäksi on vielä yksi näkymä, joka avautuu osittain viimeksi mainitun reseptin muokkaus -näkymän päälle:

* Reseptin poisto

Kaikki näkymät on toteutettu omina luokkinaan. Niiden näyttämistä hallinnoi luokka [`UI`](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/ui/ui_view.py).

## Sovelluslogiikka

Sovelluslogiikasta vastaa yksin luokka [`CookbookAppFunctions`](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/functions/cookbookapp_functions.py). Luokka toteuttaa käyttöliittymän tarvitsemat metodit datan tallennuksesta ja tietokannoista vastaavien luokkien `UserDatabase` ja `RecipesDatabase` avulla. 

Sovelluslogiikasta vastaavan luokan metodeja ovat esimerkiksi 
- `log_in(username, password)`
- `log_out()`
- `sign_in(username, password)`
- `users_recipes()`
- `add_recipes(name, instructions)`
- `modify_chosen_recipe(instructions)`
- `delete_chosen_recipe()`

## Tietojen pysyväistallennus

Kansion _datacontrol_ luokat [`RecipesDatabase`](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/datacontrol/recipes_database.py) ja [`UserDatabase`](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/datacontrol/users_database.py) vastaavat tietojen tallentamisesta ja niiden  tarpeellisesta välittämisestä sovelluslogiikasta vastaavalle `CookbookAppFunctions`-luokalle. Kumpikin luokka tallentaa tietoa SQL-tietokantaan, tauluihin `recipes` ja `users`: 
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/table_relations.png)

Taulut alustetaan [initialize_database.py](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/initialize_database.py)-tiedostossa. Luokat on mahdollista korvata muilla toteutustavoilla, kuten huomataan sovelluslogiikkaa testattaessa, jossa ei tallenneta mitään tietokantaan vaan listoihin.

## Päätoiminnallisuudet

### Käyttäjän kirjautuminen
Kun kirjautumisnäkymässä on syötetty käyttäjätunnus ja salasana (jotka siis ovat alla olevassa esimerkissä oikein, eli kirjautuminen onnistuu) ja painettu nappia "Log in", sovelluksen kontrolli etenee seuraavasti:
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/architecture_sequence_login.png)

### Uuden käyttäjän luominen
Kun kirjautumisnäkymästä siirrytään uuden käyttäjän luomiseen, uutta käyttäjää luodessa on syötetty uusi käyttäjätunnus ja salasana (ja syöte kelpaa, eli uuden käyttäjän luominen onnistuu) ja painetaan nappia "Sign in", sovelluksen kontrolli etenee seuraavasti:
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/architecture_sequence_signin.png)

### Uuden reseptin luominen 
Kun keittokirjanäkymästä siirrytään uuden reseptin luomiseen, käyttäjä (jonka id on tässä 1) on syöttänyt reseptille nimen ja ohjeet (ja syöte kelpaa) ja painetaan nappia "Create new recipe", sovelluksen kontrolli etenee seuraavasti:
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/architecture_sequence_new_recipe.png)

## Reseptiin siirtyminen
Kun käyttäjän (jonka id on tässä 1) keittokirjanäkymästä siirrytään reseptiin (jonka id on tässä 1), sovelluksen kontrolli etenee seuraavasti: 
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/architecture_sequence_recipe.png)

## Muut toiminnallisuudet
Sovelluksen kaikki toiminnallisuudet toimivat samalla periaatteella. Käyttöliittymän tapahtumakäsittelijä kutsuu tarvittavaa sovelluslogiikan funktiota, joka puolestaan kutsuu tarvittavaa tiedon tallennuksen tai muokkauksen funktiota. Käyttöliittymään palattaessa päivitetään näkymä oikeanlaiseksi.
