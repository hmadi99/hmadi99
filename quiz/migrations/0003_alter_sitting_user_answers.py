# Generated by Django 4.0.8 on 2023-11-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_choice_id_alter_progress_id_alter_question_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitting',
            name='user_answers',
            field=models.TextField(blank=True, default='', verbose_name='User Answers'),
        ),
    ]
