# Generated by Django 5.1.6 on 2025-02-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.CharField(max_length=100)),
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('doj', models.DateField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
