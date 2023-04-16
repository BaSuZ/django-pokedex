from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def Home(request):
#     return render(request, 'PokedexApp/index.html')

class Home(TemplateView):
    template_name = 'PokedexApp/index.html'