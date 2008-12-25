from django.contrib import admin
import models

class BannerInline(admin.TabularInline):
    model = models.Banner

class SlotAdmin(admin.ModelAdmin):
    inlines = [BannerInline]
admin.site.register(models.Slot, SlotAdmin)