from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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



class Profile(models.Model):
    user = models.OneToOneField(auto_created=True, on_delete=models.CASCADE, parent_link=True,
                                primary_key=True, serialize=False, to='auth.user')
    
    name = models.CharField(max_length=255, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    