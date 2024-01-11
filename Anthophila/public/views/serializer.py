from rest_framework import serializers
from anthophila_app.models import Beehive, Beeyard, Contaminated, Intervention, User


class BeeyardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beeyard
        fields = ["id", "name", "beekeeper"]


class ContaminatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contaminated
        fields = ["id", "beehive", "contamination_date",
                  "contamination_disease"]


class InterventionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Intervention
        read_only_fields = ("id",)

        fields = ['beehive', 'type_intervention', 'intervention_date']


class BeehiveSerializer(serializers.ModelSerializer):
    beeyard_extended = BeeyardSerializer(source='beeyard', read_only=True)
    contaminated_extended = ContaminatedSerializer(
        source='contaminations', many=True, read_only=True)
    intervention_extended = InterventionSerializer(
        source='interventions', many=True, read_only=True)

    class Meta:
        model = Beehive
        fields = ["id", "name", 'queen_year',
                  'bee_type', 'beeyard', 'beeyard_extended', 'contaminated_extended', 'intervention_extended']


class BeekeeperSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = ["id", "username", "public_contact"]


class BeeyardDetailedSerializer(serializers.ModelSerializer):
    beehives_extended = BeehiveSerializer(
        many=True, source='beehives', read_only=False)
    beekeeper_extended = BeekeeperSerializer(
        source='beekeeper', read_only=False)

    class Meta:
        model = Beeyard
        fields = ["id", "name", "beekeeper",
                  "beehives_extended", "beekeeper_extended"]


class BeekeeperDetailedSerializer(serializers.ModelSerializer):
    beeyard_extended = BeeyardDetailedSerializer(
        source="beeyard", read_only=True)

    class Meta:
        model = User
        read_only_fields = ("id",)

        fields = ["id", "username", "first_name",
                  "last_name", "public_contact", "beeyard_extended"]
