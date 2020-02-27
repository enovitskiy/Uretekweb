# Generated by Django 2.2.6 on 2020-02-03 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0010_auto_20200203_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsubnav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('section', models.TextField(null=True)),
                ('template_name', models.CharField(max_length=30, null=True)),
                ('subname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='information.Subnavigator')),
            ],
        ),
    ]
