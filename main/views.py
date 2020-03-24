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

def autocalculate(request):
    rows= row.objects.all()
    columns = column.objects.all()

    m = []
    name=[]
    lengths = []
    quantities = []

    for i in rows:
        m.append(int(i.available_lengths))
    for i in columns:
        name.append(i.name)
        lengths.append(int(i.length))
        quantities.append(int(i.quantity))

    
    n = len(lengths)

    for i in range(n-1):#this will sort the program
        for j in range(n-1):
            if(lengths[j]<lengths[j+1]):
                lengths[j],lengths[j+1] = lengths[j+1], lengths[j]
                quantities[j], quantities[j+1] = quantities[j+1], quantities[j]
                name[j],name[j+1] = name[j+1],name[j]

    length = lengths[:]
    quantity = quantities[:]
    dd = []
    for c in range(len(m)):
        n = len(lengths)

        dds = []
        for i in range(n): 
            used = 0
            if(quantities[i]!=0):
                for j in range(quantities[i],0,-1):
                    used = 0
                    if(m[c] - (lengths[i]*j)>=0):
                        m[c]-= (lengths[i]*j)
                        used = j
                        quantities[i] -= used
                        break
            dds.append(used)
        dds.append(m[c])
        dd.append(dds)
    return render(request, "autoresult.html", {"rows":rows,"m":m,"lengths":lengths,"quantities":quantities,"middata":dd,"name":name,"length":length,"quantity":quantity})