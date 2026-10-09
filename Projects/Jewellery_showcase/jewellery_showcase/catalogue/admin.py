from django.contrib import admin

from .models import Category, Enquiry, Jewel


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Jewel)
class JewelAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "material", "price", "is_featured", "is_available"]
    list_filter = ["category", "material", "is_featured", "is_available"]
    list_editable = ["is_featured", "is_available"]
    search_fields = ["name", "description"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "jewel", "created_at", "is_handled"]
    list_filter = ["is_handled"]
    list_editable = ["is_handled"]
    readonly_fields = ["created_at"]
