# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180522_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='_email',
            field=models.EmailField(verbose_name='e-mail address', max_length=254),
        ),
    ]
