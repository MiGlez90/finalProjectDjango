# Generated by Django 2.0.1 on 2018-02-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_auto_20171209_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='profilePictures'),
        ),
    ]
