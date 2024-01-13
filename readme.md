# Anthophila, the application for beekeepers

App created by **Gilles Helleu**

Anthophila is an application for beekeepers, enabling them not only to manage their apiaries and hives, but also to make data concerning their hives and bees publicly available.

**The host of the docker project is here : http://localhost:8002/**  
**Database creation is done on the port 5435**

## Installation

1. Clone the repertory : `git clone https://github.com/gillesah/Anthophila.git`

2. Go to the folder Anthophila : `cd Anthophila`
3. Create an .env file with the .env-template at the root of the project (Anthophila)
4. Run Docker : `docker-compose up --build`
5. Migrate (in an other terminal) `docker-compose exec web_anthophila python Anthophila/manage.py migrate`
6. Import a fictive database : `docker-compose exec web_anthophila python Anthophila/manage.py commandBDD`
7. Have a glass of hydromel and enjoy !

## Two app : anthophila_app & public

### The Anthophila_app : private app

{host}/API/ : you must be connected to see this API  
BEEKEEPERS : {host}/API/beekeepers/  
BEEHIVES : {host}/API/beekeepers/  
BEEYARDS : {host}/API/beeyards/

### Public API

{host}/public/ To have all the public data

The following data are available in the public API:

- Information on beekeepers when they have given their authorization
- information on beeyards
- information on beehives

BEEKEEPERS: {host}/API_PUBLIC/beekeepers/  
BEEHIVES: {host}/API_PUBLIC/beehives/  
BEEYARDS : {host}/API_PUBLIC/beeyards/

## Templating part

The view for the templating part is in [core.py](./anthophila_app/views/core.py)  
You can access it from the host root

## Actions at the beehive level

- change the year of birth of all the queens of all the beehives : {host}/API/beehives/{id}/change_queen/

```
{"queen_year": 2022}
```

## Actions at the beeyard (apiary) level

- change the year of birth of all the queens of all the beehives : {host}/API/beeyards/{id}/change_queens/
- add or update an contamination for all the beehives in a beeyard : {host}/API/beeyards/{id}/all_contaminated/ e.g. data :

```
{"contamination_date": "2024-01-08", "contamination_disease": " a new contamination of La fausse teigne"}
```

- Make an intervention on all the beehives in a beeyard : {host}/API/beeyards/{id}/beeyard_intervention/

## Security and permissions :

Only the beekeeper of a beehive (or a beeyard) has the permission to edit. For the other users, they can just read.

## ID and UUID

Beehives and the beekeepers have UUID as ID.

## access to the admin page

the django admin is here : {host}/bee_anthophila/
