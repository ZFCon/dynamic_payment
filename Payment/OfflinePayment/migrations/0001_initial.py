# Generated by Django 2.2 on 2020-04-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('total', models.FloatField(default=0)),
            ],
        ),
    ]
