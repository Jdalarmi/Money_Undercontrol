from django.shortcuts import get_object_or_404, redirect, render
from .forms import ComprasForm
from .models import Compras, Month
from .matplot import generate_pie_chart
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    list_category = Compras.objects.all()
    range_month = Month.objects.all()
    categories = [item.category for item in list_category]
    values = [item.value for item in list_category]
    chart_data = generate_pie_chart(categories, values)
    context ={
        'list_category':list_category,
        'chart_data':chart_data,
        'range_month':range_month
    }
    return render(request, 'index.html', context)

@login_required
def shopping(request):
    form = ComprasForm(request.POST)
    if request.method == 'POST':
        category = request.POST.get('category')
        date = request.POST.get('date')
        if request.POST.get('value') == '':
            messages.error(request, f'POR FAVOR INSIRA O CAMPO VALOR!!')
            return redirect('shopping')
        else:
            value = float(request.POST.get('value').replace(",", "."))


        data_obj = datetime.strptime(date, '%Y-%m-%d')
        month_name = data_obj.strftime('%B')

        dados_mensais, created = Month.objects.get_or_create(
            month = month_name,
            defaults={'value_all':value}
        )

        if not created:
            dados_mensais.value_all += value
       
        dados_mensais.save()

        existing_category = Compras.objects.filter(category=category).first()

        if existing_category:
            existing_category.value += value
            existing_category.save()
        else:
            Compras.objects.create(
                category=category,
                date=date,
                value= value
            )
        messages.success(request, "ADICIONADO COM SUCESSO!!!")
        
    return render(request, "shopping.html", {'form': form})

@login_required
def sale(request):
    return render(request, 'sale.html')