# Generated by Django 3.2.5 on 2021-07-03 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
                ('street', models.CharField(max_length=80, verbose_name='улица')),
                ('city', models.CharField(max_length=50, verbose_name='город')),
                ('state', models.CharField(max_length=33, verbose_name='Край/Область')),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=18)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=18)),
                ('is_default', models.BooleanField(verbose_name='Основной')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'адрес',
                'verbose_name_plural': 'адреса',
                'unique_together': {('is_default', 'user')},
            },
        ),
    ]
