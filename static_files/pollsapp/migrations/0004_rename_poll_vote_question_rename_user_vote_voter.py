# Generated by Django 4.1 on 2023-10-08 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pollsapp", "0003_rename_voter_vote"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vote", old_name="poll", new_name="question",
        ),
        migrations.RenameField(model_name="vote", old_name="user", new_name="voter",),
    ]