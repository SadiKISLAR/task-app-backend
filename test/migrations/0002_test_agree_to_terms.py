# Generated by Django 4.1.6 on 2023-02-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='agree_to_terms',
            field=models.BooleanField(default=True),
        ),
    ]
