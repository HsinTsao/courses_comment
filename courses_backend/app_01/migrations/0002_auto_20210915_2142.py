# Generated by Django 3.2.7 on 2021-09-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='term',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
