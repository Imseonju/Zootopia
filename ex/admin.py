from django.contrib import admin
from .models import LLuser, Character
from django.utils.safestring import mark_safe
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.


class DisplayCharacter(ImportExportMixin, admin.ModelAdmin):
    list_display = ('number','name','gender', 'job', 'species', 'photo', 'get_image')
    search_fields = ('name', 'job')
    list_filter = ('gender',)
    ordering = ('number',)

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height ="{height}"/>'.format(
            url = obj.photo.url,
            width = 200,
            height = 200,
        ))

admin.site.register(LLuser)
admin.site.register(Character, DisplayCharacter)