from datetime import timedelta
from inspect import currentframe
from typing import Annotated
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Count
from django.utils import timezone
from .forms import Event_form
from .forms import Speaker_form
from .forms import Participant_form
from .forms import Scheduleform
from .forms import categoryform
from django.db.models import Sum
from django.db.models import Sum, Avg, Min, Max
from .models import Category, Event_management, Speaker_management, Participant_management, Schedule_management, Payment


def json_view(request):
    data = list(Category.objects.values(), Event_management.objects.values(), Speaker_management.objects.values(), Participant_management.objects.values(), Schedule_management.objects.values(), Payment.objects.values())
    return JsonResponse(data, safe=False)


def home_view(request):
    return render(request, 'home.html')


def events_list(request):
    events = Event_management.objects.all()
    return render(request, 'event.html', {'events': events})


def speaker_list(request):
    speakers = Speaker_management.objects.all()
    return render(request, 'speaker.html', {'speakers': speakers})

def details_of_speaker(request, id):
    myevent = Speaker_management.objects.get(id=id)
    template = loader.get_template('speaker_details.html')
    context = {
          'mymember': myevent,
           }
    return HttpResponse(template.render(context,request))


def event_details(request, event_title):
    event = get_object_or_404(Event_management, title=event_title)
    return render(request, 'event_details.html', {'event': event})


def testing(request):
    speaker_names = Speaker_management.objects.values_list('name', flat=True)
    template = loader.get_template('speaker_details.html')
    context = {
        'Speaker_names': speaker_names,
    }
    return HttpResponse(template.render(context, request))


def paid_events(request):
    paid_events = Event_management.objects.filter(event_charge__gt=0)

    return render(request,'paid_events.html',{'paid_events': paid_events})


def upcoming(request):
    current_date = timezone.now().date()

    upcoming = Event_management.objects.filter(start_date__gte=current_date)
    return render(request,'upcoming.html', {'paid':upcoming})


def freeEvent(request):
    freeEvent = Event_management.objects.filter(is_free=True)
    return render(request,'freeEvent.html',{'event':freeEvent})
def upcoming(requests):
    upcoming_events = Event_management.objects.filter(start_date__gte=currentframe)
    return render(requests, 'upcoming.html', {'upcoming_events': upcoming_events})


def free_events(request):
    free_events = Event_management.objects.filter(is_free=True)
    return render(request, 'free_events.html', {'free_events': free_events})

def participants_with_all_payments(request):
    participants = Participant_management.objects.annotate(payment_count=Count('payment')).filter(payment_count=Event_management.objects.count(), payment_count__gt=0)
    return render(request, 'participants_with_all_payments.html', {'participants': participants})


def participant_list(request):
    participants = Participant_management.objects.all()
    return render(request, 'participant_details.html', {'participants': participants})


def events_details(request, event_title):
    # event = get_object_or_404(Event, title=events_title)
    event = Event_management.objects.get(title=event_title )
    return render(request, 'event_details.html', {'events': event})

def participant_names(request):
    name=Participant_management.objects.all()
    return render(request,'p_name.html',{'names':name})

def event_forms(request):
        form = Event_form(request.POST or None)
        if form.is_valid():
            form.save()
            form=Event_form() 
        context = {
            'form': form
              
        }   
        return render (request, 'Event_forms.html',{'form':form}) 
    
def speaker_forms(request):
        form = Speaker_form(request.POST or None)
        if form.is_valid():
            form.save()
            form=Speaker_form() 
        context = {
            'form': form
              
        }   
        return render (request, 'speaker_form.html',{'form':form}) 

def participant_forms(request):
    if request.method == 'POST':
        form = Participant_form(request.POST)
        if form.is_valid():
            form.save()
            form = Participant_form()
            context = {
                'form': form
            }
            return render(request, 'participant_form.html', context)
    else:
        form = Participant_form()
    
    context = {
        'form': form
    }
    return render(request, 'participant_form.html', context)
def schedule_forms(request):
   form =Scheduleform(request.POST or None)
   if form.is_valid():
            form.save()
            form=Speaker_form() 
   context = {
            'form': form
              
        }   
   return render (request, 'sheduleform.html',{'form':form})
def speaker_list(request):
    speakers = Speaker_management.objects.all()
    return render(request, 'speaker.html', {'speakers': speakers})


def display_schedule(request):
    schedules = Schedule_management.objects.all()
    return render(request, 'schedulelist.html', {'schedules': schedules})
def display_category(request):
    category= Category.objects.all()
    return render(request, 'categorylist.html', {'category': category})

def cat_forms(request):
   form =categoryform(request.POST or None)
   if form.is_valid():
            form.save()
            form=categoryform() 
   context = {
            'form': form
              
        }   
   return render (request, 'categoryform.html',{'form':form})


def all_payments(request):
    payments = Payment.objects.all()
    return render(request, 'payments_list.html', {'payments': payments})
def participant_payments(request, participant_id):
    participant = Participant_management.objects.get(id=participant_id)
    payments = Payment.objects.filter(participant=participant)
    return render(request, 'participant_payments.html', {'participant': participant, 'payments': payments})

def free_events(request):
    events = Event_management.objects.filter(is_free=True)
    return render(request, 'free_events.html', {'events': events})

def paid_events(request):
    events = Event_management.objects.filter(is_free=False)
    return render(request, 'paid_events.html', {'events': events})

def event_count(request):
    participants = Participant_management.objects.all()
    for participant in participants:
        participant.event_count = participant.payment_set.count()
    return render(request, 'event_count.html', {'participants': participants})

from django.shortcuts import render
from .models import Payment, Event_management

def total_paid_event(request, event_id):
    event = Event_management.objects.get(id=event_id)
    total_paid = Payment.objects.filter(event=event).aggregate(total=Annotated.Sum('amount_paid'))['total']
    return render(request, 'total_paid_event.html', {'event': event, 'total_paid': total_paid})

def avg_price_paid(request):
    paid_events = Event_management.objects.filter(is_free=False)
    avg_price = paid_events.aggregate(avg=Avg('payment__amount_paid'))['avg']
    return render(request, 'avg_price_paid.html', {'avg_price': avg_price})

def highest_paid_events(request):
    events = Event_management.objects.all()
    events_with_payment = [(event, Payment.objects.filter(event=event).aggregate(total=Sum('amount_paid'))['total']) for event in events]
    events_with_payment.sort(key=lambda x: x[1] if x[1] is not None else 0, reverse=True)
    return render(request, 'highest_paid_events.html', {'events_with_payment': events_with_payment})

def top_paying_participants(request):
    participants = Participant_management.objects.all()
    participants_with_payment = [(participant, Payment.objects.filter(participant=participant).aggregate(total=Sum('amount_paid'))['total']) for participant in participants]
    participants_with_payment.sort(key=lambda x: x[1] if x[1] is not None else 0, reverse=True)
    return render(request, 'top_paying_participants.html', {'participants_with_payment': participants_with_payment})

def recent_payers(request):
    recent_date = timezone.now() - timedelta(days=7)
    participants = Payment.objects.filter(payment_date__gte=recent_date).values('participant').distinct()
    return render(request, 'recent_payers.html', {'participants': participants})

def top_revenue_events(request):
    events = Event_management.objects.all()
    events_with_revenue = [(event, Payment.objects.filter(event=event).aggregate(total=Sum('amount_paid'))['total']) for event in events]
    events_with_revenue.sort(key=lambda x: x[1] if x[1] is not None else 0, reverse=True)

    return render(request, 'top_revenue_events.html', {'events_with_revenue': events_with_revenue})

def participants_paid_all(request):
    all_events = Event_management.objects.all()
    participants = Payment.objects.values('participant').distinct()
    participants_paid_all_events = []

    for participant in participants:
        paid_events = Payment.objects.filter(participant=participant['participant'])
        if paid_events.count() == all_events.count():
            participants_paid_all_events.append(participant['participant'])

    return render(request, 'participants_paid_all.html', {'participants_paid_all_events': participants_paid_all_events})