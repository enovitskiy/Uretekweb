# Generated by Django 2.2.6 on 2020-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0075_auto_20200616_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.TextField(verbose_name='РЕШЕНИЕ URETEK'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name0',
            field=models.CharField(blank=True, max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='name1',
            field=models.TextField(blank=True, verbose_name='ТРАДИЦИОННОЕ РЕШЕНИЕ'),
        ),
    ]