# Generated by Django 4.2.7 on 2023-12-26 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0139_alter_announcement_announcement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="announcement_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 26, 23, 47, 25, 444962, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date",
            ),
        ),
    ]