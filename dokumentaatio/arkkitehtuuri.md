# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmikerroksista kerrosarkkitehtuuria, jossa ylimpänä on käyttöliittymästä vastaava kerros, pakkauskaaviossa *ui*. Seuraavana on sovelluslogiikasta vastaava kerros, pakkauskaaviossa *functions*, ja alimpana on datan tallennuksesta ja tietokannasta vastaava kerros, pakkauskaaviossa *datacontrol*. 

![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/ohte_package_diagram_detail_1.png)

## Sovelluslogiikka

Sovellukselle välttämätön tietokanta muodostuu kahdesta taulusta, *users* ja *recipes*.
![](https://raw.githubusercontent.com/MillaKelhu/ot-harjoitustyo/master/dokumentaatio/kuvat/table_relations.png)

Sovelluslogiikasta vastaa yksin luokka CookbookAppFunctions. Luokka toteuttaa käyttöliittymän tarvitsemat metodit datan tallennuksesta ja tietokannoista vastaavien luokkien UserDatabase ja RecipesDatabase avulla. 

Sovelluslogiikasta vastaavan luokan metodeja ovat esimerkiksi 
- `log_in(username, password)`
- `log_out()`
- `sign_in(username, password)`
- `users_recipes()`
- `add_recipes(name, instructions)`
- `modify_chosen_recipe(instructions)`
- `delete_chosen_recipe()`

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
