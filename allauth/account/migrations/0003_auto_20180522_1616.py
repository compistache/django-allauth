# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_email_max_length'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailaddress',
            old_name='email',
            new_name='_email',
        ),
    ]
