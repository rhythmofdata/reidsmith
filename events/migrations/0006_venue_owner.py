# Generated by Django 4.1 on 2023-09-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_event_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="venue",
            name="owner",
            field=models.IntegerField(default=1, verbose_name="Venue Owner"),
        ),
    ]