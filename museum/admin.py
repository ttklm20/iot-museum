from django.contrib import admin
from .models import Artwork
from django.urls import path
from django.template.response import TemplateResponse
from config import config

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'active', 'date_display', 'timesPlayed', 'created_datetime', 'edited_datetime')
    list_editable = ('active',)
    list_filter = ('active','timesPlayed')
    list_per_page = 20
    search_fields = ('name', 'author', 'url_online', 'url_local')

    change_form_template = 'museum/admin/change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('rmngp/', self.admin_site.admin_view(self.rmngp)),
        ]
        return my_urls + urls

    def rmngp(self, request):
        context = dict(
           self.admin_site.each_context(request),
           RMNGP_API_KEY=config['rmngp']['api_key'],
        )
        return TemplateResponse(request, "museum/admin/rmngp.html", context)
