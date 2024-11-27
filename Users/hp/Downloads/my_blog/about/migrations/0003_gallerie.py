# Generated by Django 2.2.12 on 2020-06-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_contact_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallerie', models.ImageField(null=True, upload_to='gallerie/image')),
                ('titre', models.CharField(max_length=255, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Gallerie',
                'verbose_name_plural': 'Galleries',
            },
        ),
    ]
