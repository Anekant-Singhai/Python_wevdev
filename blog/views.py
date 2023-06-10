from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
# this is where the logic is actually implemented on how to handle certain routes 

# we created basic function that will serve as the home page for the user when he/she visits our site's home page

def home(request):
    return HttpResponse('<h1> Home For the Blog </h1>')

# now we need to create a urls.py file so that we can actually serve the request function that we made to the user

