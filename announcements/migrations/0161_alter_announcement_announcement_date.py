# Generated by Django 4.2.7 on 2024-01-08 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0160_alter_announcement_announcement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="announcement_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 8, 16, 42, 36, 356851, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date",
            ),
        ),
    ]
