# Generated by Django 2.2 on 2020-04-20 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0012_auto_20200420_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='discount_type',
            field=models.CharField(choices=[('percent', 'Percent'), ('price', 'Price')], default='percent', help_text='The Precent choice convert the price like that (Price(20)-Price(20)*discount(25)%)=15. The Price choice convert the price like that (Price(20)-discount(15))=5.', max_length=20),
        ),
    ]
