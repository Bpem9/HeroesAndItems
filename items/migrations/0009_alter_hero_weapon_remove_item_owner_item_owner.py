# Generated by Django 4.1.5 on 2023-01-25 13:02

from django.db import migrations, models
import django.db.models.deletion
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_alter_hero_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='weapon',
            field=models.ForeignKey(default=2, limit_choices_to=items.models.limit_weapon_choices, on_delete=django.db.models.deletion.SET_DEFAULT, to='items.item', verbose_name='Оружие'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='owner',
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ManyToManyField(null=True, related_name='owners', to='items.hero', verbose_name='Владельцы'),
        ),
    ]
