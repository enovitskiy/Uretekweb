# Generated by Django 2.2.6 on 2020-06-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0073_auto_20200616_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name0',
            field=models.TextField(blank=True),
        ),
    ]
