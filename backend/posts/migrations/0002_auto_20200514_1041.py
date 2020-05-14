# Generated by Django 3.0.6 on 2020-05-14 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post',
            new_name='json_data',
        ),
        migrations.AddField(
            model_name='posts',
            name='html_data',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]