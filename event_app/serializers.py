from rest_framework import serializers
from .models import Event_management, Category, Speaker_management, Participant_management, Payment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Event_management
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 
                  'location', 'price', 'is_free', 'available_tickets', 
                  'category', 'category_name']

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker_management
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant_management
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    participant_name = serializers.CharField(source='participant.name', read_only=True)
    event_title = serializers.CharField(source='event.title', read_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'participant', 'participant_name', 'event', 'event_title', 
                  'amount_paid', 'payment_method', 'payment_date', 'payment_status']