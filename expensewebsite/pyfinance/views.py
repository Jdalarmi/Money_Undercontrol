from django.shortcuts import get_object_or_404, redirect, render
from .forms import ComprasForm
from .models import Compras, Month
from .matplot import generate_pie_chart, generate_chart_bar
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='user_finance')
def index(request):
    user = request.user
    list_category = Compras.objects.filter(user=user)
    range_month = Month.objects.filter(user=user)
    categories = [item.category for item in list_category]
    values = [item.value for item in list_category]
    chart_data = generate_pie_chart(categories, values)
    context ={
        'list_category':list_category,
        'chart_data':chart_data,
        'range_month':range_month
    }
    return render(request, 'index.html', context)

@login_required(login_url='user_finance')
def shopping(request):
    form = ComprasForm(request.POST)
    if request.method == 'POST':
        user = request.user
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
            user=user,
            month = month_name,
            defaults={'value_all':value}
        )

        if not created:
            dados_mensais.value_all += value
       
        dados_mensais.save()

        existing_category = Compras.objects.filter(category=category, user=request.user).first()

        if existing_category:
            existing_category.value += value
            existing_category.save()
        else:
            Compras.objects.create(
                user=user,
                category=category,
                date=date,
                value= value
            )
        messages.success(request, "ADICIONADO COM SUCESSO!!!")
        
    return render(request, "shopping.html", {'form': form})


@login_required (login_url='user_finance')
def payment(request):
    if request.method == 'POST':
        payment_value = float(request.POST.get('number').replace(",", "."))
        last_object = Month.objects.last()

        if last_object:
            last_object.payment_number += payment_value
            if last_object.payment_number > last_object.value_all:
                messages.error(request, 'Não é possivel pagar valor maior que seu gasto do mês')
                return redirect('payment')
            last_object.save()

    user = request.user
    values = Month.objects.filter(user=user)
    categories = ["Gastos", "Pagar"]
    total = 0
    if values:
        for i in values:
            total = i.value_all
            number = i.payment_number
    else:
        messages.error(request, 'Por favor insira valores no mês que você esta para acessar "Pagamento"')
        return redirect('shopping')
    values = [total, number ]

    dif = total - number
      

    chart_data = generate_chart_bar(categories, values)
   
    context={
        'chart_data':chart_data,
        'total':total,
        'number':number,
        'dif':dif
    }
    return render(request, 'payment.html', context)