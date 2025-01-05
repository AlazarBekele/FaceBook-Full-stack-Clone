# Generated by Django 5.1.4 on 2025-01-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_created=True, auto_now_add=True)),
                ('First_Name', models.CharField(max_length=15)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Profile_Img', models.ImageField(upload_to='')),
                ('Bio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Story_owner', models.CharField(max_length=20)),
                ('About_story', models.CharField(max_length=20)),
                ('Story', models.ImageField(upload_to='')),
            ],
        ),
    ]
