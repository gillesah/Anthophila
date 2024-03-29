from django.contrib import admin
from .models import Beehive, Beeyard, Intervention, Contaminated, Status, Warehouse, User

class InterventionInLine(admin.TabularInline):
    model = Intervention
    extra = 1
class StatusInLine(admin.TabularInline):
    model = Status
    extra = 1
    
class BeehiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'beeyard',  'queen_year',
                    'bee_type',)
    inlines = [InterventionInLine, StatusInLine]


class ContaminatedAdmin(admin.ModelAdmin):
    list_display = ('beehive',
                    'contamination_date', 'contamination_disease',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('beehive', 'status', 'status_date',)


class BeehiveInline(admin.TabularInline):
    model = Beehive
    extra = 1


    
class BeeyardAdmin(admin.ModelAdmin):
    list_display = ('name', 'beekeeper',)
    inlines = [BeehiveInline]


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'beekeeper',)


class InterventionAdmin(admin.ModelAdmin):
    list_display = ('beehive', 'type_intervention',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name',
                    'last_name', 'public_contact', 'public_authorization')


admin.site.register(Beehive, BeehiveAdmin)
admin.site.register(Beeyard, BeeyardAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Contaminated, ContaminatedAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(User, UserAdmin)


# inline admin
