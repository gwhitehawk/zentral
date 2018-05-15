# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-15 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0012_auto_20180515_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kernelextension',
            options={'ordering': ('team__name', 'name')},
        ),
        migrations.AlterModelOptions(
            name='kernelextensionteam',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='kernelextensionpolicy',
            name='identifier',
        ),
        migrations.AddField(
            model_name='deviceartifactcommand',
            name='command_uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='kernelextensionpolicy',
            name='version',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
    ]
