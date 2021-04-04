from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя поставщика')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Товар')
    description = models.TextField(max_length=255, verbose_name='Описание товара', blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
