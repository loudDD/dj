# Generated by Django 3.1.1 on 2020-09-23 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0005_auto_20200921_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='testupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=10)),
                ('t_img', models.ImageField(upload_to='media/upload/%Y')),
            ],
        ),
    ]
