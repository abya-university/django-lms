# Generated by Django 4.2.3 on 2023-08-29 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_alter_completedlesson_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='completedlesson',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='completedlesson',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='completedlesson',
            unique_together={('user', 'lesson')},
        ),
        migrations.RemoveField(
            model_name='completedlesson',
            name='enrollment',
        ),
    ]
