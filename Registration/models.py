from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):

    EVENT_TYPE_CHOICES = [
        ('cultural', 'Cultural'),
        ('sports', 'Sports'),
        ('technical', 'Technical'),
    ]

    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)

    is_group_event = models.BooleanField(default=False)
    min_team_size = models.IntegerField(default=1)
    max_team_size = models.IntegerField(default=1)

    event_date = models.DateField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.event_type})"

    

class EventRegistration(models.Model):

    roll_no = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('roll_no', 'event')

    def __str__(self):
        return f"{self.roll_no} → {self.event.name}"


class TeamMember(models.Model):

    registration = models.ForeignKey(
        EventRegistration,
        on_delete=models.CASCADE,
        related_name='team_members'
    )

    member_name = models.CharField(max_length=100)
    member_roll_no = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.member_name




