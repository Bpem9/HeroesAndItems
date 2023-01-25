
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import *
from .serializers import *
from .services import Logistic


# ===================== Registration ===============================

# class Registration(Logistic, generics.CreateAPIView):
#     """Регистрация"""
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#
#     def post(self, request, *args, **kwargs):
#         credentials = super().create_new_user(request, *args, **kwargs)
#         super().login_new_user(request, *credentials, *args, **kwargs)
#         return redirect('create_hero')

# ===================== Character class ===============================


class HeroClassListCreateView(generics.ListCreateAPIView):
    """Отображение классов персонажей"""
    queryset = HeroClass.objects.all()
    serializer_class = HeroClassListSerializer

# ===================== Weapon Class ===============================


class WeaponClassListCreateView(generics.ListCreateAPIView):
    """Отображение классов оружия"""
    queryset = Weapon.objects.all()
    serializer_class = WeaponClassListSerializer

# ===================== Items ===============================


class ItemsListCreateView(generics.ListCreateAPIView):
    """Отображение списка шмоток"""
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ItemsCreateSerializer
        return ItemsListSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование шмотки"""
    queryset = Item.objects.all()
    # serializer_class = ItemsDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return ItemsDetailSerializer if self.request.method == 'GET' else ItemsCreateSerializer

    def put(self, request, *args, **kwargs):
        """Оружие меняет хозяина: старым хозяевам назначается оружие по-дефолту"""
        weapon = self.get_object()
        default_weapon = Item.objects.get(pk=2)
        new_owner = Hero.objects.get(pk=request.POST.get('owner'))
        new_owner.weapon = weapon
        # print('=' * 10, new_owner, '=' * 10)
        new_owner.save()
        old_owners = []
        if weapon.owner:
            old_owners.append(weapon.owner)
        else:
            old_owners = Hero.objects.filter(weapon=weapon)
        print('=' * 10, old_owners, '=' * 10)
        for owner in old_owners:
            owner.weapon = default_weapon
            # owner.save()
        return super().update(request, *args, **kwargs)

# ===================== Heroes ===============================


class HeroListView(generics.ListAPIView):
    """Отображение персонажей"""
    queryset = Hero.objects.all()
    serializer_class = HeroListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HeroCreateView(generics.CreateAPIView):
    """Создание персонажа"""
    queryset = Hero.objects.all()
    serializer_class = HeroCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data.update({'owner_id': request.user.id})
            hero = Hero.objects.create(**serializer.validated_data)
            hero.weapon.owner = hero
            hero.weapon.save()
        return redirect('update_hero', pk=hero.id)


class HeroDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Редактирование персонажа по ID"""
    queryset = Hero.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return HeroDetailSerializer if self.request.method == 'GET' else HeroUpdateSerializer

    def put(self, request, *args, **kwargs):
        """Герой меняет оружие: старому оружию хозяином назначается None, новому оружию хозяином назначается герой"""
        hero = self.get_object()
        new_weapon = Item.objects.get(pk=request.POST.get('weapon'))
        new_weapon.owner.add(hero)
        # new_weapon.save()
        old_weapon = hero.weapon
        old_weapon.owner.remove(hero)
        old_weapon.save()
        return super().update(request, *args, **kwargs)



