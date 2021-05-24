# Generated by Django 3.2.3 on 2021-05-23 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0002_callmerequest_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('phone', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('email', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('website', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Покупатель проекта',
                'verbose_name_plural': 'Покупатели проекта',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('technical_task', models.FileField(blank=True, upload_to='files/tasks')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('is_delated', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operations.customer', verbose_name='Покупатель')),
                ('developers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('expences', models.ManyToManyField(to='operations.Outcome')),
                ('payments', models.ManyToManyField(to='operations.Income')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
