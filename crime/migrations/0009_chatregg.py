# Generated by Django 3.0.3 on 2020-02-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0008_branches'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatregg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=15)),
                ('time_h_m_s', models.CharField(max_length=15)),
                ('dchatt', models.CharField(max_length=2000)),
                ('fromm', models.CharField(max_length=10)),
                ('too', models.CharField(max_length=10)),
            ],
        ),
    ]