# Generated by Django 4.1 on 2023-09-22 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="announcement_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 9, 22, 17, 52, 22, 164981, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date",
            ),
        ),
    ]