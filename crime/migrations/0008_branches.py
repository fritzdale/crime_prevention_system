# Generated by Django 3.0.3 on 2020-02-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0007_auto_20200222_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnname', models.CharField(max_length=100)),
                ('bpass', models.CharField(max_length=100)),
                ('barea', models.CharField(max_length=800)),
                ('profile', models.ImageField(upload_to='image')),
                ('nopolice', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=2000)),
            ],
        ),
    ]
