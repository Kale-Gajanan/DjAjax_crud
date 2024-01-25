# Generated by Django 4.1.10 on 2024-01-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxdj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'tblemployee',
            },
        ),
    ]
