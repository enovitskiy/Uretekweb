# Generated by Django 2.2.6 on 2020-06-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0074_auto_20200616_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name0',
            field=models.TextField(blank=True, verbose_name=''),
        ),
    ]
