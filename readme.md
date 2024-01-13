# Anthophila, the application for beekeepers

Anthophila is an application for beekeepers, enabling them not only to manage their apiaries and hives, but also to make data concerning their hives and bees publicly available.

## Two app : anthophila_app & public

### The Anthophila_app

{host}/API/ : you must be connected to see this API

### Public API

{host}/public/ To have all the public data

The following data are available in the public API:

- Information on beekeepers when they have given their authorization
- information on beeyards
- information on beehives

## Installation

1. Clone the repertory : `https://github.com/gillesah/Anthophila.git`
2. Go to the folder Anthophila : `cd Anthophila`
3. Create an .env file with the .env-template
4. Run Docker : `docker-compose up --build`
5. Migrate (in an other terminal) `docker-compose exec web_anthophila python Anthophila/manage.py migrate`
6. Import a fictive database : `docker-compose exec web_anthophila python Anthophila/manage.py commandBDD`
7. Have a glass of hydromel and enjoy !

docker-compose exec web_anthophila python Anthophila/manage.py commandBDD

docker-compose exec web_anthophila python Anthophila/manage.py migrate

## Templating part

The view for the templating part is in [core.py](./anthophila_app/views/core.py)

## usernames of beekeeper in the database

Roger  
Thierry

## Access to the data

### Beekepers

Connected : {host}/API/beekeepers/  
Not connected : {host}/API_public/beekeepers/

### Beehives

/API_PUBLIC/beehives/

### Beeyards

/API_PUBLIC/beeyards/

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

The permission setup is in the file [permission.py](./anthophila_app/views/serializer.py)

Only the beekeeper of a beehive (or a beeyard) has the permission to edit. For the other users, they can just read.

## ID and UUID

Beehives and the beekeepers have UUID as ID.

## access to the admin page

the django admin is here : {host}/bee_anthophila/
