from django.contrib import admin
from portfolio import models

# Register your models here.


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = 'user',
    search_fields = 'user__last_name',


@admin.register(models.UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = 'user', 'phone', 'status'
    search_fields = 'user__last_name', 'phone'
    list_filter = 'status',


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = 'name',