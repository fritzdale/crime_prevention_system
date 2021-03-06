# Generated by Django 3.0.3 on 2020-02-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0003_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('carea', models.CharField(max_length=800)),
                ('wip', models.CharField(max_length=500)),
                ('detail', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.AlterField(
            model_name='area',
            name='doorno',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='area',
            name='pincode',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='area',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
