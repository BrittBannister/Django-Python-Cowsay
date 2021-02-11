import subprocess

from django.shortcuts import render
from cowsplay_app.models import Cow_Model
from cowsplay_app.forms import Cow_Form

def index_view(request):
    if request.method == 'POST':
        form = Cow_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            text = data.get('text')
            Cow_Model.objects.create(
                text = text
            )
            cowtalk = subprocess.run(f'cowsay "{text}"', capture_output=True, shell=True).stdout.decode('utf-8').strip()
            form = Cow_Form()
            return render(request, 'index.html', {'form': form, 'subprocess': cowtalk})
    form = Cow_Form()
    return render(request, 'index.html', {'form': form})

def history_view(request):
    cows = Cow_Model.objects.all().order_by('-id')[:11]
    return render(request, 'history.html', {'cowsays': cows})