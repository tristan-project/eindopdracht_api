# eindopdracht_api


Voor het eindproject werk je wederom individueel een opdracht uit die je huidige kennis binnen het vak toepast, met uitbreiding. Het thema mag je zelf kiezen. 

De volledige evaluatie gebeurt op GitHub. Dit wil zeggen dat iets dat niet op GitHub staat, ook niet geëvalueerd zal worden. %-punten die je krijgt per volledige sectie liggen vast. %-punten die vervolgens afgetrokken worden voor niet-complete delen van de sectie liggen niet vast. Eigen bepaalde aanvullingen mogen natuurlijk ook!

Kies (en combineer) uit de aanvullingen zaken die je het meest interesseren. Over het algemeen is het zo dat aanvullingen met een nummer zoals 3.1.1 de aanvulling met nummer 3.1 nodig hebben om relevant te zijn of te werken.

Tijdens de oplevering geef je dan je GitHub repository links mee, je hosting links en een oplijsting van de nummers die je uitgewerkt hebt.

1. ❔ ALGEMENE EISEN & DOCUMENTATIE (alles samen +50%)

Minstens 3 GET, 1 POST, 1 PUT en 1 DELETE endpoints
ok
Minstens 3 entiteiten in je API via een SQLite databank
ok
Minstens hashing en OAuth implementeren

Beschrijving van het gekozen thema, je API(s) en je uitbreidingen + link naar de zaken die hosted zijn op GitHub README.md

Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md

Volledige OpenAPI docs screenshot(s) op GitHub README.md

https://python-service-tristan-project.cloud.okteto.net/openapi.json 

Logisch gebruik van path parameters, query parameters en body
ok

Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt
ok

Deployment van de API container(s) op Okteto Cloud via Docker Compose
ok

Test alle GET endpoints van een van je APIs via de Requests en pytest library met een testfile in de root van je repository.


2. 🔧 AANVULLINGEN: FUNCTIE

2.1 (+5%) Test alle niet-GET endpoints.
ok

2.2 (+5%) Zorg ervoor dat de testfile ook tijdens de GitHub Actions gerund wordt.
ok

3. 📳 AANVULLINGEN: FRONT-END

3.1 (+15%) Maak een front-end voor je applicatie die al je GET endpoints en POST endpoints bevat.
ok

3.1.1 (+10%) Host de front-end op Netlify. 

3.1.2 (+10%) Geef de front-end een leuke stijlgeving.
ok 

3.1.3 (+15%) Gebruik Vue, React, Angular of Svelte als JavaScript framework.

3.2 (+15%) Maak gebruik van de Grafana Cloud gratis tier om een Grafana oplossing op te zetten om je API te consumen.

4. 📝 AANVULLINGEN: DATA

4.1 (+20%) Maak een tweede versie van je originele API, maar deze keer gebruik je MongoDB Atlas i.p.v. een SQL oplossing. Je plaatst deze in een nieuwe GitHub repository, met als README.md een korte uitleg van de verschillen.

4.1.1 (+15%) Vervang MongoDB Atlas door een MongoDB container die bij in je deployment zit. Mét volume.

4.2 (+30%) Zet een ActiveMQ message queue systeem voor een endpoint van je API, dit zit tevens ook als container in je deployment.

5. 🔐 AANVULLINGEN: SECURITY

5.1 (+25%) Maak een tweede versie van je originele API, maar deze keer gebruik je Open ID Connect via Okta als Auth oplossing i.p.v. je eigen OAuth implementatie. Je plaatst deze in een nieuwe GitHub repository, met als README.md een korte uitleg van de verschillen.

5.2 (+30%) Deploy een Spring Boot Cloud Gateway (zelf geprogrammeerd) / KrakenD Gateway (zelf geconfigureerd) / Kong Gateway (zelf geconfigureerd) voor een van je APIs. Zorg ervoor dat je endpoints door de Gateway beschermd worden via een check op een token. Eventuele endpoints waarmee je authentiseert zoals /token enz. moeten natuurlijk niet gecheckt worden, aangezien je eerst een token moet kunnen bekomen.
