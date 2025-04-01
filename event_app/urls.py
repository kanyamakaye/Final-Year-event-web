from django.urls import path
from .import views
from .models import Participant_management, Payment
from django.utils import timezone

urlpatterns = [
    path('', views.home_view, name='home'),
    path('event/list', views.events_list),
    path('speaker/list/', views.speaker_list),
    path('speaker/list/details/<int:id>', views.details_of_speaker),
    path('details/', views.events_details),
    path('speakers/name', views.testing),
    path('paid/', views.paid_events, name='paid_events'),
    
    
    path('participants/all-payments/', views.participants_with_all_payments, name='participants_with_all_payments'),

    path('freeEvent/', views.free_events, name='freeEvent'),  
    path('participant/details', views.participant_list),
    path('participant/details', views.participant_list),
    path('participants/all-payments/', views.participants_with_all_payments, name='participants_with_all_payments'),
    path('participant/names',views.participant_names),
    path('event/forms',views.event_forms),
    path('speaker/forms',views.speaker_forms),
    path('participant/forms',views.participant_forms),
    path('schedule/forms',views.schedule_forms),
    path('schedule/', views.display_schedule, name='display_schedule'),
    path('cat/',views.display_category),
    path('cat/form',views.cat_forms),
    
    #All query of payment

    path('payments/', views.all_payments, name='all_payments'),
    path('participant/<int:participant_id>/payments/', views.participant_payments, name='participant_payments'),
    path('events/free/', views.free_events, name='free_events'),
    path('events/paid/', views.paid_events, name='paid_events'),
    path('event/count/', views.event_count, name='event_count'), 
    path('event/<int:event_id>/total_paid/', views.total_paid_event, name='total_paid_event'),
    path('events/avg_price_paid/', views.avg_price_paid, name='avg_price_paid'),
    path('events/highest_paid/', views.highest_paid_events, name='highest_paid_events'),
    path('participants/top_paying/', views.top_paying_participants, name='top_paying_participants'),
    path('events/top_revenue/', views.top_revenue_events, name='top_revenue_events'),
    path('participants/paid_all/', views.participants_paid_all, name='participants_paid_all'),

]
