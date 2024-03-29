# Generated by Django 4.2.5 on 2023-11-12 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('netbox_contract', '0020_alter_contract_external_partie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='external_partie',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='contracts',
                to='netbox_contract.serviceprovider',
            ),
        ),
    ]