# Generated by Django 4.2.17 on 2025-01-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_educationalresource_date_uploaded_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='health_resources/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='educationalresource',
            name='file',
            field=models.FileField(upload_to='educational_resources/'),
        ),
    ]
