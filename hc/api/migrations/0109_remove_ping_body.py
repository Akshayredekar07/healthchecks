# Generated by Django 5.0.7 on 2024-07-11 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0108_move_body_to_body_raw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ping',
            name='body',
        ),
    ]