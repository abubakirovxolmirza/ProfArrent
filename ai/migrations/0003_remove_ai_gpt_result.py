# Generated by Django 5.0.6 on 2024-05-13 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0002_ai_first_ai_second_ai_third'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ai',
            name='gpt_result',
        ),
    ]
