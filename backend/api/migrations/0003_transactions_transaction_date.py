# Generated by Django 5.0.2 on 2024-02-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bond_fixeddeposit_mutualfund_stock_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='transaction_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
