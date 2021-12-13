# Generated by Django 4.0 on 2021-12-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null='false')),
                ('body', models.TextField(null='false')),
                ('slug', models.SlugField(null='false', unique='true')),
            ],
        ),
        migrations.AlterField(
            model_name='companyposition',
            name='department_name',
            field=models.CharField(max_length=100, null='false'),
        ),
        migrations.AlterField(
            model_name='companyposition',
            name='office_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='companyposition',
            name='position_name',
            field=models.CharField(max_length=100, null='false'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100, null='false'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=125, null='false'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time_joined',
            field=models.DateField(),
        ),
    ]
