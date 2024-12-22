# Generated by Django 5.1.4 on 2024-12-22 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='books_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='users_wishlist',
            field=models.ManyToManyField(blank=True, related_name='books_wished', to=settings.AUTH_USER_MODEL),
        ),
    ]