# Generated by Django 2.2.6 on 2020-06-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0067_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name1',
            field=models.CharField(blank=True, max_length=50, verbose_name='full name'),
        ),
    ]
