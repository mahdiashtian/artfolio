from django.contrib import admin

from activities.models import ArtActivity, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class ArtActivityAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(ArtActivity, ArtActivityAdmin)
admin.site.register(Photo)
