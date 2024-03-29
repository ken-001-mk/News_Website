# Generated by Django 4.2.1 on 2023-07-09 20:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
    ]
