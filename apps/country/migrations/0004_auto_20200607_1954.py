# Generated by Django 2.2.13 on 2020-06-07 19:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0003_auto_20200607_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b200e57a-ed16-42ac-9532-01c245a40a12'), editable=False, primary_key=True, serialize=False),
        ),
    ]