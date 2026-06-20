from django.contrib import admin
from .models import Gift, Recommendation, Favorite


class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'occasion', 'recipient_type', 'is_trending')
    list_filter = ('category', 'occasion', 'recipient_type', 'is_trending')
    search_fields = ('name', 'description', 'category', 'occasion', 'recipient_type')


admin.site.register(Gift, GiftAdmin)
admin.site.register(Recommendation)
admin.site.register(Favorite)