from django.contrib import admin

# Register your models here.

# import your model
from app_cbs.models import Thing

# set up automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Thing, ThingAdmin)