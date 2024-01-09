# Anthophila, l'application pour les apiculteurs

Anthophila is an application for beekeepers, enabling them not only to manage their apiaries and hives, but also to make data concerning their hives and bees publicly available.

## Two app : anthophila_app & public

### The Anthophila_app

{host}/API/ : you must be connected to see this API

### Public API

{host}/public/ To have all the public data

## Templating part

The view for the templating part is in [core.py](./anthophila_app/views/core.py)

## usernames of beekeeper in the database

Roger  
Thierry

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
