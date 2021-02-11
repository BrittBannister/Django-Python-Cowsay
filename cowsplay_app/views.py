from django.shortcuts import render
from cowsplay_app.models import Cow_Model
from cowsplay_app.forms import Cow_Form

def index_view(request):
    # return render(request, 'index.html', {'heading': 'Welcome To Cowsplay!'})
    form = Cow_Form()
    return render(request, 'index.html', {'form': form})



def history_view(request):
    # possible way to sort and order from stack overflow-come back to this.
    # cow_obj = Cow_Model.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'cowsay': cow_obj})