# Generated by Django 2.1.2 on 2018-12-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0012_auto_20181223_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='num_tx_processed',
            field=models.DecimalField(decimal_places=4, default=0, help_text='The number of transactoins processed by the subminer for the Subscription.', max_digits=50),
        ),
    ]