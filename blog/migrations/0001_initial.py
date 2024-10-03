# Generated by Django 4.0 on 2024-10-01 17:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='foydalanuvchi ismi')),
                ('email', models.EmailField(max_length=200, verbose_name='foydalanuvchi emaili')),
                ('message', models.TextField(verbose_name='foydalanuvchi xabari')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Yanglik sarlavhasi')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Yanglik matni')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
