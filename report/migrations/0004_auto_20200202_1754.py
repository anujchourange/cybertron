# Generated by Django 3.0.2 on 2020-02-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_report_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
