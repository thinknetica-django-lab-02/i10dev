from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя поставщика')
    address = models.TextField(verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=12, blank=True)
    descriptions = models.TextField(blank=True, verbose_name='Описание продавца')
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Товар')
    description = models.TextField(
        max_length=255, verbose_name='Описание товара', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
