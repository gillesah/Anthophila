from rest_framework import serializers
from anthophila_app.models import Beehive, Beeyard, Contaminated
from django.contrib.auth.models import User


class BeeyardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beeyard
        fields = ["id", "name", "beekeeper"]


class ContaminatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contaminated
        fields = ["id", "beehive", "contamination_date",
                  "contamination_disease"]


class BeehiveSerializer(serializers.ModelSerializer):
    beeyard_extended = BeeyardSerializer(source='beeyard', read_only=True)
    contaminated_extended = ContaminatedSerializer(
        source='contaminations', many=True, read_only=True)

    class Meta:
        model = Beehive
        fields = ["id", "name", 'queen_year',
                  'bee_type', 'beeyard', 'beeyard_extended', 'contaminated_extended']


class BeeyardDetailedSerializer(serializers.ModelSerializer):
    beehives_extended = BeehiveSerializer(
        many=True, source='beehives', read_only=False)

    class Meta:
        model = Beeyard
        fields = ["id", "name", "beekeeper", "beehives_extended"]


class BeekeeperSerializer(serializers.ModelSerializer):
    beeyard_extended = BeeyardDetailedSerializer(
        source="beeyard", read_only=True)

    class Meta:
        model = User
        read_only_fields = ("id",)

        fields = ["id", "username", "email", "beeyard_extended"]
