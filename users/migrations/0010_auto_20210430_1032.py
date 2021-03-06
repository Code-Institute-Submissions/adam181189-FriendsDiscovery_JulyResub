# Generated by Django 3.2 on 2021-04-30 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_auto_20210430_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='nationality',
            field=django_countries.fields.CountryField(default='Where are you from?', max_length=150),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
