# Generated by Django 4.2.7 on 2024-07-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("letter", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscribers",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]