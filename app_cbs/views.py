from django.shortcuts import render
from app_cbs.models import Thing

# Create your views here.
def index(request):
    # defining the variable
    things = Thing.objects.all()
    # passing the variable to the view
    return render(request, 'index.html', {
        # don't forget to pass it in, and the last comma
        'things': things,
    })

def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })