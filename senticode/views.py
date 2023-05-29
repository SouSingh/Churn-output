from django.shortcuts import render
from django.http import HttpResponse
import datetime
from Backmodel.model import data
from django.http import JsonResponse


# Create your views here.
def Home(request):
    if request.method == 'POST':
        form_data = request.POST.get('form_field_name')
        code = data(form_data)
        code1 = code['label']
        score = code['score']
        scoreout = score*100
        rounds = round(scoreout, 2)
        context = {'code': code1, 'score': rounds,'text': form_data}
        return render(request, 'index.html',context=context )
    else:
        return render(request, 'index.html')

def Api(request):
    return render(request, 'Api.html')

def ApiVeiw(request, param):
    modaldata = data(param)
    return JsonResponse(modaldata)
