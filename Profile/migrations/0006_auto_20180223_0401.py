# Generated by Django 2.0.1 on 2018-02-23 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_profile_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='academicId',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='academic_program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Profile.AcademicProgram'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='curp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, related_name='profile', to='Profile.Language'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tutor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.Tutor'),
        ),
    ]