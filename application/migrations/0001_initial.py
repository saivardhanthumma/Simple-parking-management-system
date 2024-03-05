# Generated by Django 4.2.2 on 2024-03-03 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_area_no', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100, unique=True)),
                ('vehicle_limit', models.CharField(max_length=100)),
                ('parking_charge', models.CharField(max_length=200)),
                ('doc', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Add_Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=100)),
                ('parking_area_no', models.CharField(max_length=100)),
                ('parking_charge', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('arrival_time', models.DateTimeField(auto_now=True)),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.category', to_field='vehicle_type')),
            ],
            options={
                'db_table': 'Add_Vehicle',
            },
        ),
    ]