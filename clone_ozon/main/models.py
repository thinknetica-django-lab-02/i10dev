from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя поставщика')
    address = models.TextField(verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=12, blank=True)
    descriptions = models.TextField(
        blank=True, verbose_name='Описание продавца')

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
    tag = models.ManyToManyField(Tag, help_text='добавте теги')

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    def get_tags(self):
        return self.tag.all()
    
        
        # return {tag.name for tag in self.tags.all()}



class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})