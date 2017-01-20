from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count
from .models import User, Quote, Favorite

# Create your views here.
def index(request):
    # Quote.objects.all().delete()
    if ('thisUser' in request.session) == False:
        messages.add_message(request, messages.INFO, 'You must be logged in to view that page.')
        return redirect(reverse('login_reg:index'))
    else:
        id = request.session['thisUser']
        # print(id)

        quotables = Quote.objects.exclude(favorite__this_user=id).order_by('-created_at')
        context = {
        'users':User.objects.all(),
        'thisUser':User.objects.get(id=id),
        'quotes':Quote.objects.all(),
        'favorites':Favorite.objects.filter(this_user=id),
        'quotables':quotables,
        }
        return render(request, 'quotes/index.html', context)

def add(request):
    if request.method == "GET":
        if ('thisUser' in request.session) == False:
            messages.add_message(request, messages.INFO, 'You must be logged in to view that page.')
            return redirect(reverse('login_reg:index'))
        else:
            return redirect(reverse('quotes:index'))

    elif request.method == "POST":
        verify = Quote.quoteManager.create(request.POST)

        if verify[0] == False:
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('quotes:index'))

        elif verify[0] == True:
            # thisUser = request.session['thisUser']
            note = verify[1]
            print(note)
            return redirect(reverse('quotes:index'))

def favorite(request):
    if request.method == "POST":
        bridge = Quote.quoteManager.bridge_connections(request.POST)
        if bridge == True:
            print ('favorites updated')
            return redirect(reverse('quotes:index'))
        else:
            print('ERROR')
            return HttpResponse('Whoops! Something went wrong! Please try again later.')
    else:
        if ('thisUser' in request.session) == False:
            messages.add_message(request, messages.INFO, 'You must be logged in to view that page.')
            return redirect(reverse('login_reg:index'))
        else:
            return redirect(reverse('quotes:index'))

def remove(request):
    if request.method == "POST":
        destroy = Quote.quoteManager.delete(request.POST)
        if destroy == True:
            return redirect(reverse('quotes:index'))
    else:
        if ('thisUser' in request.session) == False:
            messages.add_message(request, messages.INFO, 'You must be logged in to view that page.')
            return redirect(reverse('login_reg:index'))
        else:
            return redirect(reverse('quotes:index'))



def show(request, id):
    if request.method == "GET":
        if ('thisUser' in request.session) == False:
            messages.add_message(request, messages.INFO, 'You must be logged in to view that page.')
            return redirect(reverse('login_reg:index'))
        else:
            count = Quote.objects.filter(user=id).count()
            context = {
                'user':User.objects.get(id=id),
                'favorites':Favorite.objects.all(),
                'quotes':Quote.objects.all(),
                'count':count,
            }
            return render(request, 'quotes/show.html', context)

def deleteQuote(request):
    if request.method == "POST":
        destroy = Quote.quoteManager.destroy(request.POST)
        if destroy == True:
            return redirect(reverse('quotes:index'))
    else:
        if ('thisUser' in request.session) == False:
            messages.add_message(request, messages.INFO, 'You must be logged in to view that page.')
            return redirect(reverse('login_reg:index'))
        else:
            return redirect(reverse('quotes:index'))
