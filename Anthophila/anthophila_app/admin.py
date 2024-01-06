from django.contrib import admin
from .models import Beehive, Beeyard, Intervention, Contaminated, Status


class BeehiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'beeyard',  'queen_year',
                    'bee_type',)


class ContaminatedAdmin(admin.ModelAdmin):
    list_display = ('beehive',
                    'contamination_date', 'contamination_disease',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('beehive', 'status', 'status_date',)


class BeeyardAdmin(admin.ModelAdmin):
    list_display = ('name', 'beekeeper',)


class InterventionAdmin(admin.ModelAdmin):
    list_display = ('beehive', 'type_intervention',)


admin.site.register(Beehive, BeehiveAdmin)
admin.site.register(Beeyard, BeeyardAdmin)
admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Contaminated, ContaminatedAdmin)
admin.site.register(Status, StatusAdmin)


# inline admin
