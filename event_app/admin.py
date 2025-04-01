from django.contrib import admin
from event_app.models import Category,Event_management,Speaker_management,Participant_management,Schedule_management,Payment


# Register your models here.
admin.site.register(Category)
admin.site.register(Event_management)
admin.site.register(Speaker_management)
admin.site.register(Participant_management)
admin.site.register(Schedule_management)
admin.site.register(Payment)

