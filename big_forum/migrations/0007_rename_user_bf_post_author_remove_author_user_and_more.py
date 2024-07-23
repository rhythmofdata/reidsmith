# Generated by Django 4.2.7 on 2023-12-09 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("big_forum", "0006_alter_author_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bf_post", old_name="user", new_name="author",
        ),
        migrations.RemoveField(model_name="author", name="user",),
        migrations.AddField(
            model_name="author",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]