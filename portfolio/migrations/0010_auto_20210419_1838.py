# Generated by Django 3.1.7 on 2021-04-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20210419_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
