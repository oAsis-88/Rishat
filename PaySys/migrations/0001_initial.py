# Generated by Django 4.1.3 on 2022-11-26 15:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название скидки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Скидка в сумме')),
                ('percent', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка в %')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('until_at', models.DateTimeField(verbose_name='Дата истечения')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена')),
                ('currency', models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD')], default='RUB', max_length=3, verbose_name='Валюта')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кол-во')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Заказ', max_length=50, verbose_name='Название')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('discount', models.ManyToManyField(blank=True, related_name='discount', to='PaySys.discount')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название налога')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('percent', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Налог в %')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Кол-во')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaySys.item')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PaySys.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ManyToManyField(blank=True, related_name='tax', to='PaySys.tax'),
        ),
        migrations.AddConstraint(
            model_name='discount',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('price__isnull', False), ('percent__isnull', True)), models.Q(('price__isnull', True), ('percent__isnull', False)), _connector='OR'), name='only_one_price'),
        ),
    ]
