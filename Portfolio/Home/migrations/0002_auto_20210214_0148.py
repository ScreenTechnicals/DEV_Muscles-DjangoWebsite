# Generated by Django 3.1.4 on 2021-02-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='sno',
            field=models.AutoField(default='', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
