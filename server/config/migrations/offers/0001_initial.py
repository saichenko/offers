# Generated by Django 3.2.5 on 2021-07-03 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0003_alter_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('base_price', models.PositiveIntegerField(verbose_name='цена без скидки')),
                ('discount_price', models.PositiveIntegerField(verbose_name='цена со скидкой')),
                ('discount', models.PositiveSmallIntegerField(verbose_name='скидка')),
                ('url', models.URLField(verbose_name='ссылка на товар')),
                ('description', models.TextField(verbose_name='описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.category')),
            ],
            options={
                'verbose_name': 'предложение',
                'verbose_name_plural': 'предложения',
            },
        ),
    ]
