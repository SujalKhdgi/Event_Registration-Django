from django.contrib import admin
from .models import Event, EventRegistration, TeamMember

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_type', 'is_group_event', 'event_date', 'venue')
    list_filter = ('event_type', 'is_group_event')
    search_fields = ('name',)

@admin.register(EventRegistration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'roll_no', 'event', 'email', 'phone')
    list_filter = ('event',)
    search_fields = ('full_name', 'roll_no', 'email')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('registration', 'member_name')
