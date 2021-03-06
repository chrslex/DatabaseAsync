# Generated by Django 3.0.7 on 2020-08-13 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='warna_baju',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-z A-Z/]*$', 'Only letters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='nama',
            field=models.CharField(max_length=75, validators=[django.core.validators.RegexValidator('^[a-z A-Z/]*$', 'Only letters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='panggilan',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-z A-Z/]*$', 'Only letters are allowed.')]),
        ),
    ]
