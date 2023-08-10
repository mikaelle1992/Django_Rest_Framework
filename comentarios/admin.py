from django.contrib import admin
from .models import Comentario
from .action import reprova_comentario, aprova_comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentario, aprova_comentario]
    
admin.site.register(Comentario, ComentarioAdmin)