# Generated by Django 2.2 on 2020-06-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]