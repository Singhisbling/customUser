# Generated by Django 2.0.7 on 2018-08-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BDapp', '0004_auto_20180802_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]