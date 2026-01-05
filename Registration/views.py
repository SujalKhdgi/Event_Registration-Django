from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from .models import Event, EventRegistration, TeamMember

def home(request):
    return render(request, 'Registration/index.html')

def select_event_type(request):
    event_types = Event.objects.values_list('event_type', flat=True).distinct()
    return render(request, 'Registration/event_type.html', {'event_types': event_types})

def event_list(request, event_type):
    events = Event.objects.filter(event_type=event_type)
    return render(request, 'Registration/event_list.html', {'events': events, 'event_type': event_type})

def event_register(request, event_id):
    event = Event.objects.get(id=event_id)

    if request.method == "POST":
        roll_no = request.POST['roll_no']
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']

        team_members = request.POST.getlist('team_members[]')

        # ✅ MIN validation (backend)
        if event.is_group_event:
            if len(team_members) < event.min_team_size:
                return render(request, 'Registration/register.html', {
                    'event': event,
                    'error': f"Minimum {event.min_team_size} members required"
                })

        # ✅ Save main registration
        try:
            registration, created = EventRegistration.objects.get_or_create(
                event=event,
                roll_no=roll_no,
                defaults={
                    'full_name': full_name,
                    'email': email,
                    'phone': phone
                }
            )
            if not created:
                # Already registered
                return render(request, 'Registration/register.html', {
                    'event': event,
                    'error': "You are already registered for this event!"
                })
        except IntegrityError:
            return render(request, 'Registration/register.html', {
                'event': event,
                'error': "Registration failed due to database error!"
            })

        # ✅ SAVE TEAM MEMBERS
        if event.is_group_event:
            for member in team_members:
                TeamMember.objects.create(
                    registration=registration,
                    member_name=member
                )

        return render(request, 'Registration/success.html', {
            'event': event
        })

    return render(request, 'Registration/register.html', {'event': event})