# Generated by Django 2.2.12 on 2020-06-29 13:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('elenizado', '0007_cours_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
