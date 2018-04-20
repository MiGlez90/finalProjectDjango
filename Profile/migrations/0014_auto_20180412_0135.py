# Generated by Django 2.0.1 on 2018-04-12 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0013_auto_20180411_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='certifications',
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='Profile.Profile'),
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='type',
            field=models.CharField(choices=[('CE', 'Certificado'), ('CO', 'Constancia')], default='CE', max_length=2),
        ),
    ]