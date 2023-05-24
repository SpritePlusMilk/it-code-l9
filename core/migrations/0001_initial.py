# Generated by Django 4.2.1 on 2023-05-13 07:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DomainNameServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=40)),
                ('expires', models.DateTimeField(default=datetime.datetime(2023, 6, 12, 7, 16, 36, 60766, tzinfo=datetime.timezone.utc))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='website', to='core.client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='dns_server',
            field=models.ManyToManyField(blank=True, to='core.domainnameserver'),
        ),
    ]
