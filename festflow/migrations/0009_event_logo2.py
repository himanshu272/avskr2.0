# Generated by Django 2.0.2 on 2018-10-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0008_auto_20181007_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='logo2',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
    ]
