# Generated by Django 2.1.7 on 2019-02-27 11:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0041_auto_20180927_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessunit',
            name='meta_business_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.MetaBusinessUnit'),
        ),
        migrations.AlterField(
            model_name='businessunit',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Source'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='signed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Certificate'),
        ),
        migrations.AlterField(
            model_name='enrollmentsecret',
            name='meta_business_unit',
            field=models.ForeignKey(help_text='The business unit the machine will be assigned to at enrollment', on_delete=django.db.models.deletion.PROTECT, to='inventory.MetaBusinessUnit'),
        ),
        migrations.AlterField(
            model_name='machinegroup',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Source'),
        ),
        migrations.AlterField(
            model_name='machinesnapshot',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.BusinessUnit'),
        ),
        migrations.AlterField(
            model_name='machinesnapshot',
            name='os_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.OSVersion'),
        ),
        migrations.AlterField(
            model_name='machinesnapshot',
            name='puppet_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.PuppetNode'),
        ),
        migrations.AlterField(
            model_name='machinesnapshot',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Source'),
        ),
        migrations.AlterField(
            model_name='machinesnapshot',
            name='system_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.SystemInfo'),
        ),
        migrations.AlterField(
            model_name='machinesnapshot',
            name='teamviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.TeamViewer'),
        ),
        migrations.AlterField(
            model_name='osxappinstance',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.OSXApp'),
        ),
        migrations.AlterField(
            model_name='osxappinstance',
            name='signed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.Certificate'),
        ),
        migrations.AlterField(
            model_name='puppetnode',
            name='core_facts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.PuppetCoreFacts'),
        ),
        migrations.AlterField(
            model_name='puppetnode',
            name='trusted_facts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.PuppetTrustedFacts'),
        ),
    ]
