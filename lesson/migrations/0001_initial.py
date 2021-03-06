# Generated by Django 3.0.3 on 2020-02-18 17:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=datetime.datetime(2020, 2, 18, 17, 37, 46, 171055, tzinfo=utc))),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('material_type', models.CharField(choices=[('theory', 'Theoretical'), ('practice', 'Practical')], default='theory', max_length=20)),
                ('status', models.CharField(choices=[('private', 'Draft'), ('public', 'Published')], default='private', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_materials', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
