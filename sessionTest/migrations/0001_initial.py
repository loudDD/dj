# Generated by Django 3.1.1 on 2020-09-18 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='session_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=10, unique=True)),
                ('s_password', models.CharField(max_length=20)),
                ('s_token', models.CharField(max_length=256)),
            ],
        ),
    ]