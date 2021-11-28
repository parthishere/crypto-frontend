from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from .models import CryptoModel, ContractTradeModel
from .forms import CryptoForm

def home(request):
    form = CryptoForm(request.POST or None)
    context = {}
    context['form'] = form
    lated_range = CryptoModel.objects.filter('-id')[0]
    context['data'] = lated_range
    if form.is_valid and request.POST:
        ins = form.save()
        context['ins'] = ins
        return redirect('home')
    return render(request, "index.html", context=context)