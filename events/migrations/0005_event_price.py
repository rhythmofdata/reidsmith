# Generated by Django 4.1 on 2023-09-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_alter_event_manager"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="price",
            field=models.CharField(blank=True, max_length=6, verbose_name="Price:"),
        ),
    ]