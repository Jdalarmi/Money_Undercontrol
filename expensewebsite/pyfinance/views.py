from django.shortcuts import render
from .forms import ComprasForm
from .models import Compras
def index(request):
    return render(request, 'index.html')

def shopping(request):
    form = ComprasForm(request.POST)
    if request.method == 'POST':
        category = request.POST.get('category')
        date = request.POST.get('date')
        value = request.POST.get('value')
        value = value.replace(",", ".")
        Compras.objects.create(
            category=category,
            date=date,
            value= value
        )

    return render(request, "shopping.html", {'form': form})
