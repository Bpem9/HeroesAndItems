from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemsListCreateView.as_view(), name='list_items'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='update_item'),
    path('heroes/', HeroListView.as_view(), name='list_heroes'),
    path('new_hero/', HeroCreateView.as_view(), name='create_hero'),
    path('heroes/<int:pk>/', HeroDetailView.as_view(), name='update_hero'),
    path('classes/', HeroClassListCreateView.as_view(), name='list_classes'),
    path('weapons/', WeaponClassListCreateView.as_view(), name='list_weapons'),
    # path('reg/', Registration.as_view(), name='custom_registration'),

    ]