# Generated by Django 2.2.7 on 2019-11-13 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0017_auto_20191113_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='descriptions',
        ),
        migrations.AddField(
            model_name='description',
            name='threat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='descriptions', to='animals.Threat'),
        ),
    ]