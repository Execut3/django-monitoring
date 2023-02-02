# Generated by Django 3.2 on 2023-02-02 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(blank=True, default=dict, null=True, verbose_name='List of online users')),
                ('count', models.IntegerField(default=0, verbose_name='Count of Online users')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='URLRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, verbose_name='Request URL Path')),
                ('method', models.CharField(max_length=10, verbose_name='Request Method')),
                ('status_code', models.IntegerField()),
                ('request_data', models.TextField(blank=True, default='')),
                ('response_data', models.TextField(blank=True, default='')),
                ('duration', models.FloatField(null=True, verbose_name='Duration of each request (ms)')),
                ('ip', models.CharField(blank=True, max_length=16, null=True, verbose_name='IP')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Request User')),
            ],
        ),
    ]