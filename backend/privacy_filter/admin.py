from django.contrib import admin
from .models import PF

class PFAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(PF, PFAdmin)