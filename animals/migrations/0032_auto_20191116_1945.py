# Generated by Django 2.2.7 on 2019-11-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0031_auto_20191116_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitat',
            name='plant_types',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
