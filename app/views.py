from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
from django.shortcuts import render
from .models import CryptoModel, ContractTradeModel
from .forms import CryptoForm
import requests

def home(request):
    context = {}
    if request.user.is_superuser:
        form = CryptoForm(request.POST or None)
        context['form'] = form
        try:
            lated_range = CryptoModel.objects.all().order_by('-id')[0]
            context['data'] = lated_range
        except IndexError:
            context['error'] = 'No data available'  
        if form.is_valid() and request.POST:
            if form.cleaned_data.get('min_lower_bound') >= form.cleaned_data.get('max_upper_bound'):
                return HttpResponse("Lower bound cannot be greater than or equal to Upper bound")
            current_price = float(requests.get("https://api.hotbit.io/api/v1/market.last?market=CTS/USDT").json().get('result'))
            ins = form.save()
            ins.current_value = current_price
            ins.save()
            context['ins'] = ins
            return redirect('home')
    else:
        context['data'] = "Not Authenticated"
    return render(request, "index.html", context=context)