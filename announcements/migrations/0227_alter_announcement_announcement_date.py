# Generated by Django 4.2.7 on 2024-07-12 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0226_alter_announcement_announcement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="announcement_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 12, 14, 0, 49, 992676, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date",
            ),
        ),
    ]