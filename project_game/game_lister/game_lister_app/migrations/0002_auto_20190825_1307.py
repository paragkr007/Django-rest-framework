# Generated by Django 2.1.4 on 2019-08-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_lister_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamer',
            name='score',
            field=models.CharField(max_length=100),
        ),
    ]
