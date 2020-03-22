import uuid

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import Q
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    # slug_book = models.SlugField(max_length=10, unique= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[str(self.id), ])  # id or pk , we can use any one.
        # we can use kwargs= {'pk':self.pk}


class Review(models.Model):
    # default object(from detail whatever sent) or (book).review_set.all / now object.review.all
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    review_body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review_body
