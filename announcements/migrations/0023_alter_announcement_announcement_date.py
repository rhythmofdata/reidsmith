# Generated by Django 4.1 on 2023-11-15 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0022_alter_announcement_announcement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="announcement_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 15, 21, 46, 29, 530523, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Date",
            ),
        ),
    ]