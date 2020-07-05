from django.contrib import admin

# Register your models here.
from . import models

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    
    list_display=('id','note','date')

admin.site.register(models.Note, NoteAdmin)
admin.site.register(models.User)
admin.site.register(models.Tag)