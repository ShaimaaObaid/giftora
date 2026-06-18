from django.contrib import admin
from .models import Gift, Recommendation, Favorite

# Register your models here.

admin.site.register(Gift)
admin.site.register(Recommendation)
admin.site.register(Favorite)