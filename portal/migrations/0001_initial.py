# Generated by Django 4.0 on 2021-12-11 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('position_name', models.CharField(max_length=100)),
                ('office_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('time_joined', models.DateField(auto_now_add=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.companyposition')),
            ],
        ),
    ]
