# Generated by Django 4.2 on 2023-04-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0002_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="Done",
            field=models.BooleanField(default=False),
        ),
    ]
