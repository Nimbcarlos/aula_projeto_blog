# Generated by Django 4.2.6 on 2023-10-15 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0008_sitesetup_background_color_sitesetup_footer_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetup',
            name='background_color',
        ),
        migrations.RemoveField(
            model_name='sitesetup',
            name='footer_color',
        ),
        migrations.RemoveField(
            model_name='sitesetup',
            name='header_color',
        ),
        migrations.RemoveField(
            model_name='sitesetup',
            name='menu_color',
        ),
    ]
