# Generated by Django 4.0.5 on 2022-07-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File_reg',
            fields=[
                ('File_id', models.AutoField(primary_key=True, serialize=False)),
                ('File_name', models.CharField(max_length=100)),
                ('File_path', models.CharField(max_length=100)),
                ('Upload_time', models.DateTimeField(auto_now_add=True)),
                ('Upload_user', models.CharField(max_length=60)),
                ('Recieve_user', models.CharField(max_length=60)),
                ('Encryption_status', models.BooleanField(default=False)),
            ],
        ),
    ]
