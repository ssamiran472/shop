# Generated by Django 2.2.4 on 2020-07-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_order_wishitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AddField(
            model_name='item',
            name='l_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='item',
            name='m_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='item',
            name='s_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='item',
            name='size_l',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='size_m',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='size_s',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='size_xl',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='xl_price',
            field=models.FloatField(default=0.0),
        ),
    ]
