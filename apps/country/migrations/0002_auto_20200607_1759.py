# Generated by Django 2.2.13 on 2020-06-07 17:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.UUIDField(default=uuid.UUID('52d081dc-17b2-48fb-b728-1d3f1d912274'), editable=False, primary_key=True, serialize=False),
        ),
    ]
