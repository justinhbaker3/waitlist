from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Waiter
from .forms import SignupForm

def index(request):
    context = {'form': SignupForm()}
    return render(request, 'waitlist/index.html', context)

def join(request):
    form = SignupForm(request.POST)
    if not form.is_valid():
        return HttpResponse('username is taken and/or referrer does not exist')
    referrer_username = form.cleaned_data.get('referrer')
    referrer = Waiter.objects.filter(username=referrer_username).first()
    waiter = Waiter.create(
        username=form.cleaned_data.get('username'), 
        referrer=referrer, 
    )
    waiter.save()
    if referrer != None:
        referrer.increment_score()
        referrer.save()
    return HttpResponse('successfully joined waitlist')

def getWaiter(request, username):
    waiter = get_object_or_404(Waiter.objects.filter(username=username))
    context = {'waiter': waiter}
    return render(request, 'waitlist/waiter.html', context)
