# Generated by Django 2.2.1 on 2019-05-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='default', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='default', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(max_length=100),
        ),
    ]