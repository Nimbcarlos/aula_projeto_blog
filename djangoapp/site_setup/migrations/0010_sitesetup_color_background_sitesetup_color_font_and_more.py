# Generated by Django 4.2.6 on 2023-10-15 18:38

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0009_remove_sitesetup_background_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='color_background',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None, verbose_name='Cor de fundo'),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='color_font',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None, verbose_name='Cor da Fonte'),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='color_footer',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=25, samples=None, verbose_name='Cor do rodapé'),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='color_header',
            field=colorfield.fields.ColorField(default='#9999ff', image_field=None, max_length=25, samples=None, verbose_name='Cor do cabeçalho'),
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='color_menu',
            field=colorfield.fields.ColorField(default='#ffff00', image_field=None, max_length=25, samples=None, verbose_name='Cor do menu'),
        ),
    ]
