from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
from django.shortcuts import render
from .models import ContinuousTeadeModel, CryptoModel, ContractTradeModel
from .forms import CryptoForm, ContinuousForm
import requests

def home(request):
    context = {}
    if request.user.is_superuser:
        form = CryptoForm(request.POST or None)
        context['form'] = form
        current_price = float(requests.get("https://api.hotbit.io/api/v1/market.last?market=CTS/USDT").json().get('result'))
        context['curr_price'] = current_price
        try:
            lated_range = CryptoModel.objects.all().order_by('-id')[0]
            context['data'] = lated_range
        except IndexError:
            context['error'] = 'No data available'  
        if form.is_valid() and request.POST:
            if form.cleaned_data.get('min_lower_bound') >= form.cleaned_data.get('max_upper_bound'):
                return HttpResponse("Lower bound cannot be greater than or equal to Upper bound")
            if form.cleaned_data.get('min_lower_bound') <= 0 or form.cleaned_data.get('max_upper_bound') <= 0:
                return HttpResponse("Lower bound or Upper bound can not be zero and less than zero")
            ins = form.save()
            ins.current_value = float(requests.get("https://api.hotbit.io/api/v1/market.last?market=CTS/USDT").json().get('result'))
            ins.save()
            
            context['ins'] = ins    
            return redirect('home')
    else:
        context['data'] = "Not Authenticated"
    return render(request, "index.html", context=context)


def continuous_view(request):
    context = {}
    if request.user.is_superuser:
        form = ContinuousForm(request.POST or None)
        context['form'] = form
        MARKET_SUMMERY_TODAY = "https://api.hotbit.io/api/v1/market.status_today"
        market = 'CTS/USDT'
        response = float(requests.get("{}?market={}".format(MARKET_SUMMERY_TODAY, market)).json().get('result').get('volume'))
        context['curr_vol'] = response
        try:
            instance = ContinuousTeadeModel.objects.all().order_by('-id')[0]
            context['data'] = instance
        except IndexError:
            context['error'] = 'No data available'  
        if form.is_valid() and request.POST:
            if form.cleaned_data.get('volume24h') <= 0 or form.cleaned_data.get('volume24h') < response:
                return HttpResponse("volume not valid")
            ins = form.save()
            
            context['ins'] = ins    
            return redirect('ctrade')
        
    else:
        context['data'] = "Not Authenticated"
    return render(request, "trade.html", context=context)
    