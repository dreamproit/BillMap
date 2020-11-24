# Generated by Django 3.1 on 2020-11-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_auto_20201113_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='related_bills',
        ),
        migrations.AddField(
            model_name='bill',
            name='related_bills',
            field=models.JSONField(default=list),
        ),
        migrations.AlterUniqueTogether(
            name='sponsor',
            unique_together={('name', 'bioguide_id')},
        ),
    ]