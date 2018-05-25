# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    EmailAddress = apps.get_model('account', 'EmailAddress')
    for email_address in EmailAddress.objects.all():
        _, domain = email_address._email.split('@')
        email_address.email = email_address._email
        email_address.domain = domain
        email_address.save()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_emailaddress_email'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
