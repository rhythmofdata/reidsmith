# Generated by Django 4.2.7 on 2023-12-28 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0010_alter_event_options_remove_event_price_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eventprice", old_name="product", new_name="event",
        ),
    ]