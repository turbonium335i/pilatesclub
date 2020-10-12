from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'registered', 'id')
    search_fields = ('name',)

class WordAdmin(admin.ModelAdmin):
    list_display = ('vocab', 'meaning', 'frequency', 'id')
    search_fields = ('vocab', 'meaning')

admin.site.site_header = 'Pilates Club'

admin.site.register(client, ClientAdmin)
admin.site.register(sale)
admin.site.register(lesson)
admin.site.register(instructor)
admin.site.register(word, WordAdmin)


