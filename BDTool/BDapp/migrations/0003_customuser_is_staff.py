# Generated by Django 2.0.7 on 2018-08-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BDapp', '0002_auto_20180802_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
