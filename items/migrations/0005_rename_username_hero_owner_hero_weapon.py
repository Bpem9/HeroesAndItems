# Generated by Django 4.1.5 on 2023-01-21 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_hero_username_alter_item_weapon_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='username',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='hero',
            name='weapon',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='items.item', verbose_name='Оружие'),
        ),
    ]
