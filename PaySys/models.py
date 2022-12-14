from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q
from django.urls import reverse


class Discount(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название скидки")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Скидка в сумме",
                              validators=[MinValueValidator(1)])
    percent = models.PositiveIntegerField(null=True, blank=True, verbose_name="Скидка в %",
                                          validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата создания')
    until_at = models.DateTimeField(verbose_name='Дата истечения')

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}#{self.id}"

    def clean(self):
        """Ensure that only one of `price` and `percent` can be set."""
        if self.price and self.percent:
            raise ValidationError("Only one price/percent field can be set.")

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        # Ограничение в БД
        constraints = [
            models.CheckConstraint(
                check=(Q(price__isnull=False) & Q(percent__isnull=True)) | (
                        Q(price__isnull=True) & Q(percent__isnull=False)),
                name='only_one_price',
            )
        ]


class Tax(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название налога")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    percent = models.PositiveIntegerField(verbose_name="Налог в %",
                                          validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}#{self.id}"

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'


class Item(models.Model):
    RUSSIA = 'RUB'
    AMERICA = 'USD'
    CUR_CHOICES = [
        (RUSSIA, "RUB"),
        (AMERICA, "USD"),
    ]

    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена",
                              validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CUR_CHOICES, default=RUSSIA, verbose_name="Валюта")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кол-во")
    created_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}#{self.id}"

    def get_absolute_url(self):
        return reverse('paysys:viewItemId', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    name = models.CharField(max_length=50, default=f"Заказ", blank=True, verbose_name="Название")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")
    created_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата создания')

    discount = models.ManyToManyField('PaySys.Discount', blank=True, verbose_name='Скидка', related_name="discount")
    tax = models.ManyToManyField('PaySys.Tax', blank=True, verbose_name='Налог', related_name="tax")

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}#{self.id}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItems(models.Model):
    item = models.ForeignKey('PaySys.Item', on_delete=models.CASCADE, verbose_name="Продукт")
    order = models.ForeignKey('PaySys.Order', on_delete=models.CASCADE, verbose_name="Заказ")
    count = models.PositiveIntegerField(verbose_name="Кол-во")

    def __str__(self):
        return f"{self.order}_{self.item}"

    def __unicode__(self):
        return f"{self.order}_{self.item}#{self.id}"

    class Meta:
        verbose_name = 'Продукты заказа'
        verbose_name_plural = 'Продукты заказа'
