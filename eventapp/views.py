from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import dataform

def index(request):
    events = Event.objects.all
    context = {
        'events': events
    } 
    return render(request,'index.html',context)

def eventdetail(request,pk):
    event_single = Event.objects.get(pk=pk)
    if request.method == "POST":
        form = dataform(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.event = event_single
            data.save()
    form = dataform()
    context = {
        'event': event_single,
        'form':form
    }
    return render(request,'details.html',context)