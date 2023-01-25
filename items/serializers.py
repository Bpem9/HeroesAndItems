
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


# ===================== Registration ===============================

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

# ===================== Character class ===============================

class HeroClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroClass
        exclude = ['slug', ]

# ===================== Weapon Class ===============================

class WeaponClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        exclude = ['slug', ]


# ===================== Items ===============================

class ItemsListSerializer(serializers.ModelSerializer):
    weapon_category = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()

    class Meta:
        model = Item
        exclude = ['id', ]


class ItemsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        # exclude = ['owner', ]


class ItemsDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = '__all__'

# ===================== Heroes ===============================


class HeroListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    hero_class = serializers.StringRelatedField()
    weapon = serializers.StringRelatedField()

    class Meta:
        model = Hero
        exclude = ['slug', 'owner', 'name', 'title' ]

    def get_full_name(self, obj):
        return f'{obj.name} {obj.title}'


class HeroCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        exclude = ['slug', 'owner' ]


class HeroDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    full_name = serializers.SerializerMethodField()
    hero_class = serializers.StringRelatedField()
    weapon = serializers.StringRelatedField()

    class Meta:
        model = Hero
        exclude = ['slug', 'name', 'title' ]

    def get_full_name(self, obj):
        return f'{obj.name} {obj.title}'


class HeroUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        exclude = ['slug', ]



