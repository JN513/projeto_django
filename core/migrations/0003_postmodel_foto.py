# Generated by Django 4.2 on 2023-04-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_postmodel_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="postmodel",
            name="foto",
            field=models.FileField(blank=True, upload_to=""),
        ),
    ]
