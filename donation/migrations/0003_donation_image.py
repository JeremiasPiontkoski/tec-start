# Generated by Django 4.2.6 on 2023-10-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_donation_date_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='image',
            field=models.ImageField(default=None, upload_to='donations/images/%Y/%m/%d', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
