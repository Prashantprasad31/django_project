# Generated by Django 5.0.1 on 2024-02-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_carttable_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carttable',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
