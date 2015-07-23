# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_auto_20141007_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partneraddress',
            name='title',
            field=models.CharField(blank=True, max_length=64, verbose_name='Title', choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='cost_price',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], max_digits=12, blank=True, null=True, verbose_name='Cost Price'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='price_excl_tax',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], max_digits=12, blank=True, null=True, verbose_name='Price (excl. tax)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='price_retail',
            field=models.DecimalField(decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], max_digits=12, blank=True, null=True, verbose_name='Price (retail)'),
            preserve_default=True,
        ),
    ]
