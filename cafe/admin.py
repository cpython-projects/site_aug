from django.contrib import admin
from .models import DishCategory, Dish, Gallery, Reservation, ContactInfoItem, Event
from django.utils.safestring import mark_safe


admin.site.register(Reservation)
admin.site.register(ContactInfoItem)
admin.site.register(Event)
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_visible', 'photo_src_tag',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Gallery photo'


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_display_links = ('id', 'name')
    list_display = ('id', 'category', 'name', 'position', 'price', 'is_visible', 'photo_src_tag',)
    list_editable = ('category', 'position', 'price', 'is_visible')
    list_filter = ('category', 'price')
    search_fields = ('name', )

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Dish photo'

