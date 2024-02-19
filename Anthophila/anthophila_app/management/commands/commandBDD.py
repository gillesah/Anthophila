from django.core.management.base import BaseCommand, CommandError
from anthophila_app.models import User, Beehive, Contaminated, Status, Beeyard, Warehouse, Intervention
from django.db import transaction

class Command(BaseCommand):
    help = "Importing data for solo project"

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            # Create users (beekeepers)
            beekeeper1 = User.objects.create(
                username='beekeeper1',
                email='beekeeper1@example.com',
                public_contact='contact1@example.com',
                public_authorization = True,
            )
            beekeeper2 = User.objects.create(
                username='Thierry',
                email='tr@g.com',
                public_contact='contact2@example.com',
                public_authorization = False,

            )
            beekeeper3 = User.objects.create(
                username='Roger',
                email='rbouzan@g.com',
                public_contact='maruche@example.com',
                public_authorization = True,

            )
               # Création des ruchers (Beeyards)
            beeyard1 = Beeyard.objects.create(
                name='Mon Rucher 1',
                beekeeper=beekeeper1
            )
            beeyard2 = Beeyard.objects.create(
                name='Mon Rucher 2',
                beekeeper=beekeeper2
            )
            beeyard3 = Beeyard.objects.create(
                name='Mon Rucher 3',
                beekeeper=beekeeper3
            )


            # Création des ruches (Beehives)
            beehive1 = Beehive.objects.create(
                name='RU2390',
                beeyard=beeyard1,
                queen_year=2021,
                bee_type='Abeille noire'
            )
            beehive2 = Beehive.objects.create(
                name='Ruche 2',
                beeyard=beeyard1,
                queen_year=2022,
                bee_type='Abeille italienne'
            )
            beehive3 = Beehive.objects.create(
                name='RU2401',
                beeyard=beeyard2,
                queen_year=2019,
                bee_type='Abeille italienne'
            )
            beehive4 = Beehive.objects.create(
                name='RU2401',
                beeyard=beeyard2,
                queen_year=2019,
                bee_type='Abeille italienne'
            )
            beehive5 = Beehive.objects.create(
                name='RU5824',
                beeyard=beeyard3,
                queen_year=2019,
                bee_type='Abeille noire'
            )
            beehive6 = Beehive.objects.create(
                name='RU9824',
                beeyard=beeyard3,
                queen_year=2018,
                bee_type='Abeille italienne'
            )
            beehive7 = Beehive.objects.create(
                name='RU1374',
                beeyard=beeyard3,
                queen_year=2023,
                bee_type='Abeille noire'
            )
            beehive8 = Beehive.objects.create(
                name='RU09238',
                beeyard=beeyard2,
                queen_year=2020,
                bee_type='Abeille noire'
            )
            beehive8 = Beehive.objects.create(
                name='RU12945',
                beeyard=beeyard1,
                queen_year=2019,
                bee_type='Abeille italienne'
            )
            beehive9 = Beehive.objects.create(
                name='RU12945',
                beeyard=beeyard1,
                queen_year=2019,
                bee_type='Abeille italienne'
            )
            beehive11 = Beehive.objects.create(
                name='RU28495',
                beeyard=beeyard2,
                queen_year=2019,
                bee_type='Abeille italienne'
            )
            beehive12 = Beehive.objects.create(
                name='RU28495',
                beeyard=beeyard1,
                queen_year=2019,
                bee_type='Abeille italienne'
            )
            beehive12 = Beehive.objects.create(
                name='RU13059',
                beeyard=beeyard2,
                queen_year=2020,
                bee_type='Abeille autrichienne'
            )


            # Intervention
            intervention = Intervention.objects.create(
                beehive=beehive1,
                type_intervention='check_sante',
                intervention_date='2023-01-01'
            )
            intervention2 = Intervention.objects.create(
                beehive=beehive2,
                type_intervention='distribution_sirop',
                intervention_date='2023-01-01'
            )
            intervention3 = Intervention.objects.create(
                beehive=beehive2,
                type_intervention='distribution_sirop',
                intervention_date='2023-01-01'
            )

            # Statut
            status = Status.objects.create(
                beehive=beehive2,
                status='Activité',
                status_date='2023-01-06'
            )

            # contamination
            contaminated = Contaminated.objects.create(
                beehive=beehive1,
                contamination_date='2023-01-10',
                contamination_disease='Varroa Destructor'
            )

            self.stdout.write(
                self.style.SUCCESS('Data has been imported successfully')
            )

        except Exception as e:
            raise CommandError(f"Error during data import: {str(e)}")
