from django.shortcuts import render, redirect

from .models import Listing
# Create your views here.
from .forms import ListingForm

#CRUD create, retrieve, update, delete 'list'



def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {'listing': listing}
    
    return render(request, 'listing.html', context)

def listing_create(request):
    #bellow how to handling the posts values
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')
            
    context = {
        'form': form
    }
    return render(request, 'listing_create.html', context)
    
def listing_uptdate(request):
    
    listing = Listing.objects.get(id=pk)
    
    #with 'instance' we pick only what we fetch , here listing
    form = ListingForm(instance = listing)
    
    if request.method == 'POST':
        form = ListingForm(request.POST, instance = listing)
        if form.is_valid():
           form.save()
           return redirect('/')
            
    context = {
        'form': form
    }
    return render(request, 'listing_update.html', context)
    