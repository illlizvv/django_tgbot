# Generated by Django 4.2.8 on 2023-12-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='body5',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
