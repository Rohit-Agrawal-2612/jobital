# Generated by Django 3.2.8 on 2022-05-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220513_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='batch',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]
