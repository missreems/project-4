# Generated by Django 2.2.7 on 2019-11-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20191113_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='diet',
            field=models.CharField(choices=[('HE', 'Herbivore'), ('OM', 'Omnivore'), ('CA', 'Carnivore')], default='OM', max_length=9),
        ),
    ]
