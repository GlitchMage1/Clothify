from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name',)
    ordering = ('id', )

admin.site.register(Category, CategoryAdmin)





class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'price', 'category', 'purchase_count', 'created_at')
    search_fields = ('name',)
    ordering = ('-id',)
    fields = ('name', 'slug', 'description', 'full_description', 'price', 'image', 'category')
    readonly_fields = ('created_at',)


admin.site.register(Product, ProductAdmin)
