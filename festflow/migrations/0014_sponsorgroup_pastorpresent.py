# Generated by Django 2.0.2 on 2018-10-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0013_auto_20181019_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorgroup',
            name='pastorpresent',
            field=models.CharField(blank=True, default='past', max_length=100),
        ),
    ]