# Generated by Django 3.1.5 on 2021-12-15 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0002_message_archived'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-timestamp',)},
        ),
    ]