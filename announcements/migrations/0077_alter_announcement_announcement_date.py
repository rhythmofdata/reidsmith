# Generated by Django 4.2.7 on 2023-12-09 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0076_alter_announcement_announcement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="announcement_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 9, 16, 7, 6, 114769, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date",
            ),
        ),
    ]
