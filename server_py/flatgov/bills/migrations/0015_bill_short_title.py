# Generated by Django 3.1 on 2020-11-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0014_bill_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='short_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]