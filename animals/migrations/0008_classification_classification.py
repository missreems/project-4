# Generated by Django 2.2.7 on 2019-11-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0007_auto_20191113_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='classification',
            name='classification',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
