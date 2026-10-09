from django.contrib import admin

from .models import Category, Product, StockTransaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "sku", "category", "quantity", "reorder_level", "unit_price"]
    list_filter = ["category"]
    search_fields = ["name", "sku"]


@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ["created_at", "product", "movement_type", "quantity", "performed_by"]
    list_filter = ["movement_type"]
    readonly_fields = ["created_at"]
