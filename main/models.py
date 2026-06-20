from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    category = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)
    recipient_type = models.CharField(max_length=100, default="General")
    is_trending = models.BooleanField(default=False)

    image = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    occasion = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=8, decimal_places=2)

    recipient_type = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)