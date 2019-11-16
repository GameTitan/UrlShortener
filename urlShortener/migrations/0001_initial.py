# Generated by Django 2.2.3 on 2019-07-09 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import urlShortener.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkTo', models.URLField()),
                ('key', models.CharField(default=urlShortener.models.Url.generateKey, max_length=20, unique=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
