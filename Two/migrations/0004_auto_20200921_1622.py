# Generated by Django 3.1.1 on 2020-09-21 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0003_animal_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Two.animal')),
                ('d_eat', models.CharField(max_length=20)),
            ],
            bases=('Two.animal',),
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='d_name',
            new_name='d_leg',
        ),
    ]