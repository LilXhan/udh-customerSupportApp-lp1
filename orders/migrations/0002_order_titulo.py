# Generated by Django 5.0.6 on 2024-07-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='titulo',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
