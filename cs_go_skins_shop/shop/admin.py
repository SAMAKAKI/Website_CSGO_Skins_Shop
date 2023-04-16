from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *


class SkinsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'availability', 'amount', 'amount_likes', 'amount_dislikes', 'amount_orders', 'appearance', 'is_stattrak', 'category', 'quality', 'get_html_photo')
    list_display_links = ('id', )
    search_fields = ('title', 'id', 'price')
    list_editable = ('availability', 'is_stattrak')
    list_filter = ('availability', 'time_create', 'is_stattrak')
    fields = ('title', 'price', 'photo', 'get_html_photo', 'float', 'availability', 'amount', 'amount_likes', 'amount_dislikes', 'amount_orders', 'pattern', 'appearance', 'is_stattrak', 'category', 'quality', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, skin_object):
        if skin_object.photo:
            return mark_safe(f'<img src="{skin_object.photo.url}" width="50">')

    get_html_photo.short_description = 'Skin mini-photo'


class ProfilesInline(admin.StackedInline):
    model = Profiles
    can_delete = False
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'


class CustomizedUserAdmin(UserAdmin):
    inlines = (ProfilesInline, )


admin.site.register(Skins, SkinsAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Profiles)
