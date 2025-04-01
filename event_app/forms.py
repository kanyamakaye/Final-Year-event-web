from django import forms
from .models import Event_management
from .models import Speaker_management
from .models import Participant_management
from .models import Schedule_management
from .models import Category
class Event_form(forms.ModelForm):
    class Meta:
        model = Event_management
        fields = ['title', 'description', 'start_date', 'end_date', 'location', 'category', 'is_free']
        
class Speaker_form(forms.ModelForm):
    class Meta:
        model = Speaker_management
        fields = ['name', 'biography', 'photo', 'email', 'phone_number', 'linkedin_link', 'twitter_link']
        
class Participant_form(forms.ModelForm):
    class Meta:
        model = Participant_management
        fields = ['name', 'email','phone_number']
        
class Scheduleform(forms.ModelForm):
    class Meta:
          model = Schedule_management
          fields = ['event','start_time','end_time','topic','speaker']


class categoryform(forms.ModelForm):
    class Meta:
          model = Category
          fields = ['name']
            

