# Generated by Django 4.1 on 2023-10-08 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0012_alter_announcement_announcement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="announcement_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 8, 23, 11, 8, 477723, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date",
            ),
        ),
    ]