# Generated by Django 2.0.1 on 2018-04-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_auto_20180322_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='suburb',
            field=models.CharField(default='', max_length=100),
        ),
    ]
