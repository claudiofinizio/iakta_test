from django.shortcuts import render

# Create your views here.
def index(request):
    page = 'travels/index.html'
    context={}
    context['ciao']='hello'
    return render(request, page, context)