# Generated by Django 4.1.6 on 2023-02-06 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_data_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='data',
        ),
    ]
