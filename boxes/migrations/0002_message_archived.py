# Generated by Django 3.1.5 on 2021-03-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boxes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
