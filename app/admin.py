from django.contrib import admin
from .models import Footer, MainMenuItem

@admin.register(MainMenuItem)
class MainMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'is_anchor', 'url', 'is_visible', 'position')
    list_editable = ('is_anchor', 'url', 'is_visible', 'position')

admin.site.register(Footer)
