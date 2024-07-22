# Generated by Django 4.1 on 2023-09-01 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyClubUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254, verbose_name="User Email")),
            ],
        ),
        migrations.CreateModel(
            name="Venue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Venue Name")),
                ("address", models.CharField(max_length=300)),
                ("zip_code", models.CharField(max_length=15, verbose_name="Zip Code")),
                (
                    "phone",
                    models.CharField(max_length=25, verbose_name="Contact Phone"),
                ),
                ("web", models.URLField(verbose_name="Website Address")),
                (
                    "email_address",
                    models.EmailField(max_length=50, verbose_name="Email"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Event Name")),
                ("event_date", models.DateTimeField(verbose_name="Event Date")),
                ("manager", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True)),
                (
                    "attendees",
                    models.ManyToManyField(blank=True, to="events.myclubuser"),
                ),
                (
                    "venue",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.venue",
                    ),
                ),
            ],
        ),
    ]
