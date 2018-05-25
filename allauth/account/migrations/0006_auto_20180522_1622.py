# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import oml.crypto.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_encrypt_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='email',
            field=oml.crypto.fields.EncryptedField(verbose_name='e-mail address'),
        ),
    ]
