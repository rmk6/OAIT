# Generated by Django 4.2.13 on 2024-05-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_reviev_review_rename_surname_resume_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ManyToManyField(to='portfolio.skill', verbose_name='требуемые навыки'),
        ),
    ]
