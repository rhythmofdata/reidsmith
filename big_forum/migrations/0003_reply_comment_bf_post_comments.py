# Generated by Django 4.2.7 on 2023-11-27 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("big_forum", "0002_category_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reply",
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
                ("content", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="big_forum.author",
                    ),
                ),
            ],
            options={"verbose_name_plural": "replies",},
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("replies", models.ManyToManyField(blank=True, to="big_forum.reply")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="big_forum.author",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bf_post",
            name="comments",
            field=models.ManyToManyField(blank=True, to="big_forum.comment"),
        ),
    ]