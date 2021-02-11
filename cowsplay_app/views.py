from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html', {'heading': 'Welcome To Cowsplay!'})


def history_view(request):
    # model info here(objects.all() stuff)
    return render(request, 'history.html', {'message':'Test Message'})