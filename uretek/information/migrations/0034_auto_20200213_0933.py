# Generated by Django 2.2.6 on 2020-02-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0033_pagenext'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagenext',
            name='titlecoloumn',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pagenext',
            name='urlvideo',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
