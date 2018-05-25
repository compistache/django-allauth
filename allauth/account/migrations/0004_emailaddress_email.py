# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import oml.crypto.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180522_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailaddress',
            name='email',
            field=oml.crypto.fields.EncryptedField(verbose_name='e-mail address', null=True),
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='domain',
            field=models.CharField(max_length=200, blank=True, null=True, editable=False),
        ),
    ]
