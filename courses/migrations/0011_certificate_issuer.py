# Generated by Django 4.2.3 on 2023-11-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0010_certificate"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="issuer",
            field=models.CharField(default="Abya", max_length=200),
            preserve_default=False,
        ),
    ]
