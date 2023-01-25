from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(HeroClass)
class HeroClassAdmin(admin.ModelAdmin):
    pass
