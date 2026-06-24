from django.contrib import admin
from .models import Profile
from .models import DiaryEntry
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date_joined',)
    search_fields = ('user__username',)


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('title','user','mood','created_date','updated_date',)
    list_filter = ('mood','created_date',)
    search_fields = ('title','content',)
    ordering = ('-created_date',)