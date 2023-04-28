from django.shortcuts import render

# Create your views here.
import datetime
def built_filters(request):
    dt=datetime.datetime.now()
    d={'data':'DONt bEliVe ThE GOd','dt':dt,'c':0}


    return render(request,'built_filters.html',d)
