# Generated by Django 2.2 on 2020-06-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranmodel', '0002_auto_20200630_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
