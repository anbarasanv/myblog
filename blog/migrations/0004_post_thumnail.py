# Generated by Django 2.1.7 on 2019-02-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190223_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
