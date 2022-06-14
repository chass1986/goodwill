from django.contrib import admin
from .models import OrgUnit


class OrgUnitAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrgUnit, OrgUnitAdmin)
