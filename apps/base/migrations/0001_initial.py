# Generated by Django 5.2.3 on 2025-07-07 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория еды',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foods_title', models.CharField(max_length=155, verbose_name='Вид еды')),
                ('title', models.CharField(max_length=155, verbose_name='Название еды')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка еды')),
                ('description', models.TextField(verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='base.category_food', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
    ]
