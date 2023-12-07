from django.shortcuts import get_object_or_404, redirect, render
from .forms import ComprasForm
from .models import Compras
from .matplot import generate_pie_chart

def index(request):
    list_category = Compras.objects.all()
    categories = [item.category for item in list_category]
    values = [item.value for item in list_category]
    
    chart_data = generate_pie_chart(categories, values)

    return render(request, 'index.html',{'chart_data':chart_data})

def shopping(request):
    form = ComprasForm(request.POST)
    if request.method == 'POST':
        category = request.POST.get('category')
        date = request.POST.get('date')
        value = float(request.POST.get('value').replace(",", "."))

        existing_category = get_object_or_404(Compras, category=category)

        if existing_category:
            existing_category.value += value
            existing_category.save()
        else:
            Compras.objects.create(
                category=category,
                date=date,
                value= value
            )
    return render(request, "shopping.html", {'form': form})
