# Generated by Django 3.2.8 on 2022-05-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_job_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
