# Generated by Django 5.0.3 on 2024-03-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default='replace me'),
            preserve_default=False,
        ),
    ]