# Generated by Django 3.0.3 on 2020-02-26 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0009_chatregg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcriminalls',
            name='Email',
        ),
    ]