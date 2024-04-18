from django.shortcuts import render
from django.http import HttpResponse
from item.models import Item, Category
from .forms import SignUpForm 

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    category = Category.objects.all()
    return render(request, 'index.html', {'items': items, 'category': category})

def signup(request):
    form = SignUpForm()  # Define the form object here
    if request.method == 'POST':  # Check request method instead of form.method
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    return render(request, 'signup.html', {'form': form})    

def contact(request):
    return render(request, 'contact.html')
