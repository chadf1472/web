# Generated by Django 2.1.2 on 2018-10-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contribution',
            name='tx_id',
        ),
        migrations.AddField(
            model_name='contribution',
            name='from_address',
            field=models.CharField(default='0x0', help_text='The wallet address tokens are sent from.', max_length=255),
        ),
        migrations.AddField(
            model_name='contribution',
            name='gas_price',
            field=models.DecimalField(decimal_places=4, default=0, help_text='The amount of token used to incentivize subminers.', max_digits=50),
        ),
        migrations.AddField(
            model_name='contribution',
            name='nonce',
            field=models.DecimalField(decimal_places=0, default=0, help_text='The of the subscription metaTx.', max_digits=50),
        ),
        migrations.AddField(
            model_name='contribution',
            name='period_seconds',
            field=models.DecimalField(decimal_places=0, default=0, help_text='The number of seconds thats constitues a period.', max_digits=50),
        ),
        migrations.AddField(
            model_name='contribution',
            name='to_address',
            field=models.CharField(default='0x0', help_text='The wallet address tokens are sent to.', max_length=255),
        ),
        migrations.AddField(
            model_name='contribution',
            name='token_address',
            field=models.CharField(default='0x0', help_text='The token address to be used with the Subscription.', max_length=255),
        ),
        migrations.AddField(
            model_name='contribution',
            name='token_amount',
            field=models.DecimalField(decimal_places=4, default=1, help_text='The promised contribution amount per period.', max_digits=50),
        ),
    ]