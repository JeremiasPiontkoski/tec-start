# Generated by Django 4.2.6 on 2023-10-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]