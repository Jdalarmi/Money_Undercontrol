import base64
from io import BytesIO
from django.shortcuts import get_object_or_404, redirect, render
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from .forms import ComprasForm
from .models import Compras

def generate_pie_chart(categories, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.axis('equal') 

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f'data:image/png;base64,{image_base64}'

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
