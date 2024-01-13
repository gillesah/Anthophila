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
                username='beekeeper2',
                email='beekeeper2@example.com',
                public_contact='contact2@example.com',
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

            # Création des ruches (Beehives)
            beehive1 = Beehive.objects.create(
                name='Ruche 1',
                beeyard=beeyard1,
                queen_year=2021,
                bee_type='Abeille noire'
            )
            beehive2 = Beehive.objects.create(
                name='Ruche 2',
                beeyard=beeyard2,
                queen_year=2022,
                bee_type='Abeille italienne'
            )

            # Création d'une intervention
            intervention = Intervention.objects.create(
                beehive=beehive1,
                type_intervention='check_sante',
                intervention_date='2023-01-01'
                # Ajoutez d'autres champs nécessaires
            )

            # Création d'un statut (Status)
            status = Status.objects.create(
                beehive=beehive2,
                status='Activité',
                status_date='2023-01-01'
            )

            # Création d'un enregistrement de contamination
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
