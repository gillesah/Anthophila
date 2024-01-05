from django.contrib import admin
from .models import Beehive, Beeyard, Intervention


class BeehiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'beeyard', 'status', 'status_date', 'queen_age',
                    'bee_type', 'contaminated', 'contamination_date')


class BeeyardAdmin(admin.ModelAdmin):
    list_display = ('name', 'beekeeper',)


class InterventionAdmin(admin.ModelAdmin):
    list_display = ('beehive', 'type_intervention',)


admin.site.register(Beehive, BeehiveAdmin)
admin.site.register(Beeyard, BeeyardAdmin)
admin.site.register(Intervention, InterventionAdmin)
