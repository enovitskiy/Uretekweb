# Generated by Django 2.2.6 on 2020-06-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0071_pagenext_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagenext',
            options={'ordering': ['order'], 'verbose_name': 'Иинформация страницы', 'verbose_name_plural': 'Иинформация страницы'},
        ),
    ]
