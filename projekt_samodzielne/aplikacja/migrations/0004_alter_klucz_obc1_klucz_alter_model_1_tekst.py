# Generated by Django 5.1.2 on 2024-10-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0003_klucz_obc1_klucz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klucz_obc1',
            name='klucz',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='model_1',
            name='tekst',
            field=models.CharField(max_length=100),
        ),
    ]
