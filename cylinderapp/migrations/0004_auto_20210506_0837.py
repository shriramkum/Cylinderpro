# Generated by Django 2.0 on 2021-05-06 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cylinderapp', '0003_auto_20210506_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cylinder',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
