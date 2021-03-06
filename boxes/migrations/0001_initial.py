# Generated by Django 3.1.5 on 2021-01-25 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Box",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100)),
                ("text", models.TextField()),
                (
                    "card_color",
                    models.CharField(
                        choices=[
                            ("BLUE", "Blue"),
                            ("RED", "Red"),
                            ("YELLOW", "Yellow"),
                            ("GREEN", "Green"),
                            ("BLACK", "Black"),
                            ("DEFAULT", "Default"),
                        ],
                        default="DEFAULT",
                        max_length=10,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now=True)),
                (
                    "box",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="boxes.box"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="box",
            name="members",
            field=models.ManyToManyField(blank=True, to="boxes.Member"),
        ),
    ]
