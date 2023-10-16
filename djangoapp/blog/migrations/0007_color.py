# Generated by Django 4.2.6 on 2023-10-15 17:13

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
                ('header_color', colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None)),
                ('menu_color', colorfield.fields.ColorField(default='#ffff00', image_field=None, max_length=25, samples=None)),
                ('footer_color', colorfield.fields.ColorField(default='#000000', image_field=None, max_length=25, samples=None)),
            ],
            options={
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
            },
        ),
    ]