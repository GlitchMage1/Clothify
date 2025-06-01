from django.contrib import admin
from reviews.models import *

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user', 'rating')
    ordering = ('-created_at',)

admin.site.register(Review, ReviewAdmin)


