# Generated by Django 5.0.1 on 2024-01-05 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anthophila_app', '0007_rename_queen_age_beehive_queen_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beehive',
            name='beeyard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beehives', to='anthophila_app.beeyard'),
        ),
        migrations.AlterField(
            model_name='contaminated',
            name='beehive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contaminations', to='anthophila_app.beehive'),
        ),
        migrations.AlterField(
            model_name='status',
            name='beehive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='anthophila_app.beehive'),
        ),
    ]
