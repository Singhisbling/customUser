# Generated by Django 2.0.7 on 2018-08-03 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BDapp', '0005_auto_20180802_0919'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
