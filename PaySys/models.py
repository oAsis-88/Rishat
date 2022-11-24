from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}#{self.id}"

    def get_absolute_url(self):
        return reverse('paysys:viewItemId', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        # managed = False  # Не создает таблицу при миграции
