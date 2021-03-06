# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import zentral.contrib.monolith.models


class Migration(migrations.Migration):

    dependencies = [
        ('monolith', '0017_manifest_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkginfo',
            name='requires',
            field=models.ManyToManyField(related_name='required_by', to='monolith.PkgInfoName'),
        ),
        migrations.AlterField(
            model_name='submanifestattachment',
            name='file',
            field=models.FileField(blank=True, upload_to=zentral.contrib.monolith.models.attachment_path),
        ),
        migrations.AlterField(
            model_name='submanifestattachment',
            name='type',
            field=models.CharField(choices=[('configuration_profile', 'configuration_profile'), ('package', 'package'), ('script', 'script')], max_length=32),
        ),
    ]
