# Generated by Django 2.1.5 on 2020-09-02 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='subject',
        ),
    ]
