# Generated by Django 3.1 on 2020-09-19 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0002_auto_20200918_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='id_person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Two.person'),
        ),
    ]
