from django.http import HttpResponse
from datetime import datetime

def natal(request):
    hoje = datetime.today().strftime('%d/%m')
    if hoje == '25/12':
        return HttpResponse("É Natal.")
    elif hoje == '21/04':
        return HttpResponse("É Tiradentes.")
    else:
        return HttpResponse("É dia comun.")
