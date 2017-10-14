from django.shortcuts import render
from app_cbs.models import Thing

# Create your views here.
def index(request):
    # defining the variable
    things = Thing.objects.filter(name__contains='Samsung')
    # passing the variable to the view
    return render(request, 'index.html', {
        # don't forget to pass it in, and the last comma
        'things': things,
    })