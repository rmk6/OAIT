# Generated by Django 4.2.13 on 2024-05-22 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_review_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='emloyer',
            new_name='employer',
        ),
    ]
