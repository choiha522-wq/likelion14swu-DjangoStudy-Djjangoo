from django.contrib import admin
from burgers.models import Burgers

@admin.register(Burgers)
class BurgersAdmin(admin.ModelAdmin):
    pass
# Register your models here.
