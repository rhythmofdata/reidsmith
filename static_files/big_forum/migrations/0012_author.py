# Generated by Django 4.2.7 on 2023-12-12 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("big_forum", "0011_bf_post_fullname"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("fullname", models.CharField(blank=True, max_length=40)),
                ("slug", models.SlugField(blank=True, max_length=400, unique=True)),
                ("bio", tinymce.models.HTMLField()),
                ("points", models.IntegerField(default=0)),
                (
                    "profile_pic",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        default=None,
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=100,
                        scale=None,
                        size=[50, 80],
                        upload_to="authors",
                    ),
                ),
                (
                    "author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
