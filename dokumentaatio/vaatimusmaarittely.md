# Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovelluksen tarkoituksena on mahdollistaa sukupuiden luominen, muokkaus ja tarkastelu.

### Käyttäjät

Ainakin alkuvaiheessa käyttäjiä on vain yhdentyyppisiä. Käyttäjä voi luoda, muokata ja tarkastella tekemäänsä sukupuuta.

### Sovelluksen toiminnallisuudet

##### Perustason toiminnallisuudet

* Uuden käyttäjätunnuksen luominen sovellukseen
  * Käyttäjätunnuksen on oltava uniikki, muuten annetaan virheilmoitus
  * Käyttäjän tulee luoda salasana
* Sovellukseen voi kirjautua e.m. tunnuksella ja salasanalla
  * Virheelliset kirjautumistiedot antavat virheilmoituksen
* Sovelluksesta voi kirjautua ulos
* Uuden sukupuun luominen
  * Tämä aloitetaan lisäämällä sukupuuhun tasan yksi henkilö (käytetään tästä myöhemmin nimitystä _juurihenkilö_), josta puuta lähdetään laajentamaan
  * Sukupuu näkyy ainoastaan sen luoneelle käyttäjälle
* Henkilölle voi lisätä vanhemmat, joille voi lisätä vanhemmat, jne.
  * Tämän toiminnallisuuden yhteydessä puhutaan vain biologisista vanhemmista, mihin liittyy rajoite siitä, että vanhempia voi olla korkeintaan kaksi
* Henkilöille voidaan määritellä nimi
* Sukupuuta voi tarkastella graafisen käyttäjäliittymän kautta

#### Toiminnallisuuden jatkokehitys

* Sukupuuhun voi lisätä muita perhesuhteita vanhempi-lapsi -dynamiikan lisäksi:
  * Sisarukset, joiden kautta voidaan myös määritellä:
    * Biologisesti sukua olevat tädit ja enot/sedät
    * Serkut
  * Aviopuolisot, joita voi olla ollut useampia. Tämän kautta päästään määrittelemään myös:
    * Isä- ja äitipuolet
    * Sisar- ja velipuolet
* Sukupuusta voidaan poistaa (muita kuin juuri-)henkilöitä, ja tietyin ehdoin näihin henkilöihin lisäksi liittyneet henkilöt poistuvat samalla
  * Jos henkilö X on molempien vanhempiensa ainoa lapsi, eikä kukaan tämän vanhemmista, isovanhemmista, yms. ole em. _juurihenkilö_, X:n mukana poistuvat myös tämän vanhemmat, isovanhemmat, yms.
  * Jos henkilö X:n jälkeläisistä alkavassa linjassa ei ole em. _juurihenkilöä_ tai tämän puolisoa, ja X on jälkeläisten ainoa vanhempi, tällaisten jälkeläisten linja poistuu henkilö X:n mukana.
  * Jos henkilö X:n puoliso ei ole mitään biologista sukua em. _juurihenkilölle_, tämä puoliso ja puolison sukulaiset poistuvat X:n mukana.   
* Sukupuu kykenee tunnistamaan ja kertomaan eri henkilöiden väliset sukulaisuussuhteet
* Sukupuun henkilöihin voidaan liittää nimen lisäksi erinäisiä tietoja:
  * Syntymävuosi ja -paikka
  * Mahdollinen kuolinvuosi -paikka
  * Sukupuoli
  * Asuinpaikka
  * Kuva, mahdollisesti useampia
  * Avioliitot
  * Ammatti
  * Koulutus
  * Kiinnostuksenkohteet tai harrastukset
  * Yms.
* Henkilön nimeä tai muita tietoja voidaan muokata
* Sukupuusta voidaan hakea tiettyjä henkilöitä esim. nimen perusteella
* Aikojen tarkistus, mm. seuraavissa tapauksissa:
  * Syntymä- tai kuolinvuodeksi ei voida määritellä vuotta tulevaisuudesta
  * Vanhemman syntymävuoden on oltava ennen lapsen syntymävuotta
    * Lisäksi syntymävuoden on oltava vähintäänkin esim. 15 vuotta ennen lapsen syntymää
  * Vanhemman kuolinvuoden on oltava lapsen syntymävuonna tai sen jälkeen
    * Pienenä poikkeuksena isät, mutta näidenkään kuolinaika ei voi olla paljoa yli 9 kuukautta ennen lapsen syntymää
  * Aviopuolisoiden avioliiton solmimisen ajankohta on molemmilla puolisoilla sama. Sama pätee mahdollisen eron ajankohtaan.
* Sukupuun voi poistaa
* Sukupuita voi luoda useita
* Käyttäjätunnuksen (ja sen mukana käyttäjätunnukseen liittyvät sukupuut) voi poistaa
* Sukupuusta voidaan eristää tarkasteltavaksi esimerkiksi:
  * Vain yksi suora äiti- tai isälinja
  * Vain henkilö X:n vanhemmat, isovanhemmat ym. ja/tai jälkeläiset
  * Vain elossa olevat henkilöt
