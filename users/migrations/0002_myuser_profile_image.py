# Generated by Django 4.2.1 on 2023-05-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="profile_image",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]