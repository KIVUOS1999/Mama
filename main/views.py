from django.shortcuts import render
from .models import row, column
from django.http import HttpResponse

def homepage(request):
    m= list()
    return render(request, 'home.html', {"rows":row.objects.all(),"columns":column.objects.all(),"ans":m})

def add(request):
    m = []
    dd = []
    
    rows = row.objects.all()
    columns = column.objects.all()
    for i in rows:
        summ=0
        dds = []
        for j in columns:  
            
            retriveddata = (request.GET[str(i.id)+str(j.id)])
            if retriveddata == "":
                data = 0
            else:
                data = int(retriveddata)
            dds.append(str(data))
            summ = summ+data*int(j.length)
        dds.append(str(i.available_lengths - summ))
        dd.append(dds)
        

    return render(request, "ans.html", {"rows":row.objects.all,"columns":column.objects.all,"ans1":m, "middata":dd})
