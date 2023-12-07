from django.shortcuts import get_object_or_404, redirect, render
from .forms import ComprasForm
from .models import Compras
from .matplot import generate_pie_chart
from datetime import datetime

range_month ={
    'Janeiro':0.0,
    'Fevereiro':0.0,
    'Março':0.0,
    'Abril':0.0,
    'Maio':0.0,
    'Junho':0.0,
    'Julho':0.0,
    'Agosto':0.0,
    'Setembro':0.0,
    'Outubro':0.0,
    'Novembro':0.0,
    'Dezembro':0.0,
}

def index(request):
    list_category = Compras.objects.all()
    categories = [item.category for item in list_category]
    values = [item.value for item in list_category]
    chart_data = generate_pie_chart(categories, values)
    context ={
        'list_category':list_category,
        'chart_data':chart_data,
        'range_month':range_month
    }
    return render(request, 'index.html', context)

def shopping(request):
    form = ComprasForm(request.POST)
    if request.method == 'POST':
        category = request.POST.get('category')
        date = request.POST.get('date')
        value = float(request.POST.get('value').replace(",", "."))

        data_obj = datetime.strptime(date, '%Y-%m-%d')

        month_number = data_obj.month
        if month_number == 1:
            range_month['Janeiro']+=value

        if month_number == 1:
            range_month['Fevereiro']+=value

        if month_number == 1:
            range_month['Março']+=value

        if month_number == 1:
            range_month['Abril']+=value
        
        if month_number == 1:
            range_month['Maio']+=value
        
        if month_number == 1:
            range_month['Junho']+=value
        
        if month_number == 1:
            range_month['Julho']+=value
        
        if month_number == 1:
            range_month['Agosto']+=value

        if month_number == 1:
            range_month['Setembro']+=value

        if month_number == 1:
            range_month['Outubro']+=value

        if month_number == 1:
            range_month['Novembro']+=value
            
        if month_number == 11:
            range_month['Dezembro']+=value


            print(range_month)
        existing_category = get_object_or_404(Compras, category=category)


        if existing_category:
            existing_category.value += value
            #existing_category.save()
        else:
            # Compras.objects.create(
            #     category=category,
            #     date=date,
            #     value= value
            # )
            ...
    return render(request, "shopping.html", {'form': form})

