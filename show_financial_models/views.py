from django.shortcuts import render
from .models import FinancialModel

def index(request):
    models = FinancialModel.objects.all()
    return render(request, 'index.html', {'models': models})
