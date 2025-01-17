# Generated by Django 4.2.17 on 2025-01-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_educationalresource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalresource',
            name='date_uploaded',
        ),
        migrations.AlterField(
            model_name='educationalresource',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='educationalresource',
            name='description',
            field=models.TextField(default='No description provided'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='educationalresource',
            name='file',
            field=models.FileField(upload_to='resources/'),
        ),
        migrations.AlterField(
            model_name='educationalresource',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
