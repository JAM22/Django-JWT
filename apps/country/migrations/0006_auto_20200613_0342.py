# Generated by Django 2.2.13 on 2020-06-13 03:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0005_auto_20200607_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9ac1e220-0415-4539-8653-6631940e2682'), editable=False, primary_key=True, serialize=False),
        ),
    ]
