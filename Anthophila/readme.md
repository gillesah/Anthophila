# Anthophila, l'application pour les apiculteurs

Application concernant l'apiculture ayant les deux objectifs principaux suivants :

- Permettre aux apiculteurs de gérer leur cheptel de ruches
- Mettre à disposition publiquement les données concernant les ruches et les abeilles

## usernames of beekeeper in the database

Roger  
Thierry

## Actions at the beeyard (apiary) level

- change the year of birth of all the queens of all the beehives : {host}/API/beeyards/{id}/change_queens/
- add or update an contamination for all the beehives in a beeyard : {host}/API/beeyards/{id}/all_contaminated/
- Make an intervention on all the beehives in a beeyard : {host}/API/beeyards/{id}/beeyard_intervention/
