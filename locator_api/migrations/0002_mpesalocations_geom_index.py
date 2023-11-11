# Generated by Django 4.2.4 on 2023-08-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locator_api", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="mpesalocations",
            index=models.Index(fields=["geom"], name="geom_index"),
        ),
    ]