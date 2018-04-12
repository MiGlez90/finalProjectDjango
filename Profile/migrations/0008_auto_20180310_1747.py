# Generated by Django 2.0.1 on 2018-03-10 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_auto_20180223_0615'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nationality',
        ),
        migrations.RemoveField(
            model_name='option',
            name='academic_program',
        ),
        migrations.RemoveField(
            model_name='option',
            name='college',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='languages',
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='Profile.Profile'),
        ),
        migrations.AddField(
            model_name='certificationtype',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='priority_index',
            field=models.CharField(blank=True, choices=[('1', 'FIRST OPTION'), ('2', 'SECOND OPTION'), ('3', 'THIRD OPTION')], default='1', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='certifications',
            field=models.ManyToManyField(blank=True, related_name='profile', to='Profile.CertificationType'),
        ),
        migrations.AddField(
            model_name='profile',
            name='wallPicture',
            field=models.ImageField(blank=True, null=True, upload_to='wallPictures'),
        ),
        migrations.AddField(
            model_name='subject',
            name='academic_program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='Profile.AcademicProgram'),
        ),
        migrations.AddField(
            model_name='subject',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='Profile.Option'),
        ),
    ]
