# Generated by Django 3.2.3 on 2021-05-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0010_rename_hearts_heart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='new_post',
            field=models.TextField(max_length=300),
        ),
    ]
