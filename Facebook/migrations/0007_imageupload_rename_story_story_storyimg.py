# Generated by Django 5.1.4 on 2025-01-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook', '0006_story_story_alter_story_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Picture/')),
            ],
        ),
        migrations.RenameField(
            model_name='story',
            old_name='Story',
            new_name='StoryIMG',
        ),
    ]
