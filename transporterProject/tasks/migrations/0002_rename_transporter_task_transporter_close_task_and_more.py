# Generated by Django 4.1.6 on 2023-02-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='transporter',
            new_name='transporter_close_task',
        ),
        migrations.AddField(
            model_name='task',
            name='transporter_open_task',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]