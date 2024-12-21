from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="books/%y/%m/%d/")
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(
        get_user_model(), related_name="books", on_delete=models.CASCADE
    )
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["isbn", "-publish"])]
        ordering = ["-publish"]

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
