# Generated by Django 2.0.2 on 2019-12-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0014_sponsorgroup_pastorpresent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='url',
            field=models.URLField(blank=True, default='#'),
        ),
    ]