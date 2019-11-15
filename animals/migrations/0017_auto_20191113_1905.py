# Generated by Django 2.2.7 on 2019-11-13 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0016_auto_20191113_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='animals',
        ),
        migrations.RemoveField(
            model_name='description',
            name='threats',
        ),
        migrations.RemoveField(
            model_name='habitat',
            name='summary',
        ),
        migrations.AddField(
            model_name='animal',
            name='descriptions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='animals', to='animals.Description'),
        ),
    ]