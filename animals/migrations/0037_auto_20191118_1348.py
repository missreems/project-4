# Generated by Django 2.2.7 on 2019-11-18 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0036_auto_20191117_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='facts',
            new_name='fact',
        ),
    ]
