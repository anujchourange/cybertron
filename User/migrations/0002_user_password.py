# Generated by Django 3.0.2 on 2020-02-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1234568, max_length=50),
        ),
    ]