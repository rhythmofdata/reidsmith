# Generated by Django 4.2.7 on 2023-11-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("big_forum", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.TextField(default="description"),
        ),
    ]