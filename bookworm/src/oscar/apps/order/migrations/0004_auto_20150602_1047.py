# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20150113_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='title',
            field=models.CharField(blank=True, max_length=64, verbose_name='Title', choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='title',
            field=models.CharField(blank=True, max_length=64, verbose_name='Title', choices=[(b'Mr', 'Mr'), (b'Mrs', 'Mrs')]),
            preserve_default=True,
        ),
    ]
