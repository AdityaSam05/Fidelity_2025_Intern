# Generated by Django 5.1.6 on 2025-02-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]
