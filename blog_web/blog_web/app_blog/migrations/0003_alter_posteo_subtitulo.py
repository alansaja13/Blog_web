# Generated by Django 4.0.4 on 2022-06-24 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_posteo_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='subtitulo',
            field=models.CharField(max_length=120),
        ),
    ]
