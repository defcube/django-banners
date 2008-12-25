from django.contrib import admin
import models

class BannerInline(admin.TabularInline):
    model = models.Banner

class SlotAdmin(admin.ModelAdmin):
    inlines = [BannerInline]
    list_display = ('name', 'get_absolute_url')
admin.site.register(models.Slot, SlotAdmin)