# Generated by Django 4.2.2 on 2023-06-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaraunt', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='person',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
