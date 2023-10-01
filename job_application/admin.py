from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    ordering = ("first_name",)
    search_fields = ('first_name', 'last_name')
    list_filter = ('date', 'occupation')
    readonly_fields = ('first_name', 'last_name')


admin.site.register(Form, FormAdmin)
