# Generated by Django 2.2.7 on 2019-11-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0026_auto_20191114_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='diet',
            field=models.CharField(choices=[('HE', 'Herbivore'), ('OM', 'Omnivore'), ('CA', 'Carnivore')], max_length=20),
        ),
    ]
