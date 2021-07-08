# Generated by Django 3.2.5 on 2021-07-03 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='offers/images/', verbose_name='изображение')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='offers.offer', verbose_name='предложение')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
            },
        ),
    ]