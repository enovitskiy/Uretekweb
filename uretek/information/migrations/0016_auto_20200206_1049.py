# Generated by Django 2.2.6 on 2020-02-06 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0015_auto_20200206_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footercont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('classname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='footer',
            name='subname',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='footersub', to='information.Navconstruct'),
        ),
        migrations.AddField(
            model_name='footer',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='information.Footercont'),
        ),
    ]