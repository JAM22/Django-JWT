# Generated by Django 2.2.13 on 2020-06-07 19:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0004_auto_20200607_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dc11099c-d964-48fe-9e78-38daafae4f1e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
