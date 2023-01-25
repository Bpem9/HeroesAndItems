
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify


def limit_weapon_choices():
    limit = ~(Q(rarity='Freakin\'Legendary') & ~Q(owner=None))
    return limit


class Item(models.Model):
    CHOICES = [
        ('Common', 'Common'),
        ('Not so common', 'Not so common'),
        ('Actually, rare', 'Actually, rare'),
        ('Freakin\'Legendary', 'Freakin\'Legendary'),
    ]
    name = models.CharField(max_length=150, verbose_name='Название')
    weapon_category = models.ForeignKey('Weapon', on_delete=models.SET_DEFAULT, default='Неизвестная валына',
                                        verbose_name='Класс оружия', related_name='items')
    descr = models.TextField(verbose_name='Описание', blank=True)
    rarity = models.CharField(choices=CHOICES, verbose_name='Рарность', max_length=20)
    # owner = models.ForeignKey('Hero', null=True, on_delete=models.SET_NULL, verbose_name='Владелец')
    owner = models.ManyToManyField('Hero', null=True, verbose_name='Владельцы', related_name='owners')
    price = models.IntegerField(blank=True, verbose_name='Цена')

    def __str__(self):
        if self.rarity == 'Freakin\'Legendary':
            return f'{self.name}, owned by {self.owner}' if self.owner else f'{self.name}, owned by John Doe'
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Hero(models.Model):
    # owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь-владелец', related_name='character')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=35, verbose_name='Имя')
    title = models.CharField(max_length=50, unique=True, verbose_name='Титул/прозвище')
    slug = models.SlugField(max_length=100, unique=True, blank=True, db_index=True, verbose_name='URL')
    hero_class = models.ForeignKey('HeroClass', null=True, on_delete=models.SET_NULL, verbose_name='Класс героя', default=1)
    lore = models.TextField(blank=True, verbose_name='История')
    strength = models.IntegerField(blank=True, verbose_name='Сила')
    agility = models.IntegerField(blank=True, verbose_name='Ловкость')
    intellect = models.IntegerField(blank=True, verbose_name='Интеллект')
    weapon = models.ForeignKey('Item',
                               default=2,
                               on_delete=models.SET_DEFAULT,
                               verbose_name='Оружие',
                               limit_choices_to=limit_weapon_choices
                               )

    def __str__(self):
        return f'{self.name} {self.title} ({self.owner.username})'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self))
        super().save(*args, **kwargs)



class HeroClass(models.Model):
    name = models.CharField(max_length=20)
    descr = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(max_length=20, unique=True, blank=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Weapon(models.Model):
    name = models.CharField(max_length=20)
    descr = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(max_length=20, unique=True, blank=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
