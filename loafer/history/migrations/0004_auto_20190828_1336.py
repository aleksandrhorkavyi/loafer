# Generated by Django 2.2.4 on 2019-08-28 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_phrase_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phrase',
            options={'ordering': ['position', 'date_create']},
        ),
    ]