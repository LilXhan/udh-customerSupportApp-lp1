# Generated by Django 5.0.6 on 2024-07-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='actualizado',
            field=models.BooleanField(default=False),
        ),
    ]