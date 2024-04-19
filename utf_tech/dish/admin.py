from django.contrib import admin

from .models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['category', 'is_vegan', 'is_special', 'code',
                    'name_ru', 'description_ru', 'cost', 'is_publish']
    list_filter = ['category', 'code', 'name_ru', 'cost', 'is_publish']
    search_fields = ['category', 'name_ru', 'is_publish']
    list_per_page = 5


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'order_id']
    list_filter = ['name_ru', 'order_id']
    search_fields = ['name_ru', 'order_id']
    list_per_page = 5
