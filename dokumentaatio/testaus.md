# Testausdokumentti

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
`CookbookAppFunctions`-luokkaa testataan [`TestCookBookAppFunctions`](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/tests/functions_tests/cookbookapp_functions_test.py)-testiluokalla. Testauksessa `CookbookAppFunctions`-luokalle injektoidaan pysyväistallennuksen sijasta muistiin tallentavat oliot `FakeUserDatabase` ja `FakeRecipesDatabase`.

### Datacontrol-luokat
Luokkia `RecipesDatabase` ja `UserDatabase` testataan testiluokilla [`TestRecipesDatabase`](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/tests/datacontrol_tests/recipes_database_test.py) ja [`TestUserDatabase`](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/src/tests/datacontrol_tests/users_database_test.py). Testeissä käytetään ainoastaan niissä käytössä olevia tiedostoja, joiden nimet on konfiguroitu _.test.env_-tiedostoon. 

### Testikattavuus
Haarautumakattavuus on 100%.
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/testikattavuus.png)

## Järjestelmätestaus

### Asennus
Sovellus on asennettu ja testattu [käyttöohjeen](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) mukaisesti Linux-ympäristössä. 

### Toiminnallisuus
Kaikki käyttöohjeen ja [vaatimusmäärittelyn](https://github.com/MillaKelhu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) esittelemät toiminnallisuudet on käyty läpi, myös virheellisillä syötteillä, kuten tyhjällä tai 10 000 merkkiä pitkällä merkkijonolla. 
