# Generated by Django 4.2.4 on 2023-09-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_variation_orderproduct_variations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
