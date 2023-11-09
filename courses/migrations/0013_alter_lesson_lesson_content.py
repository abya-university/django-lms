# Generated by Django 4.2.3 on 2023-11-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0012_lesson_word_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="lesson_content",
            field=models.TextField(
                blank=True,
                help_text="Enter the course content in Markdown format.",
                max_length=10000,
                null=True,
                verbose_name="Lesson Content",
            ),
        ),
    ]
