from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
import requests
from geopy.distance import geodesic as GD
import pandas as pd
from subprocess import run,PIPE
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        fs = FileSystemStorage()
        fs.delete(file.name)
        fs.save(file.name, file)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form':form})








def button(request):  #this will render to show the execute button
    return render(request, 'home.html')

def output():       #will render when the user clicks of execute and will give output
    data = requests.get("https://reqres.in/api/users")
    print(data.text)
    data = data.text
    return render(requests,'home.html', {'data':data})

def external(request):
    try:
     print("Hello");
     rad =request.POST.get('radius')
     lat= request.POST.get('latitude')
     long= request.POST.get('longitude')

     path_excel = "media\VillageDetails.xlsx"
     df = pd.read_excel(path_excel)
     Vle_coordinates = []
     Vle_coordinates.append(float(lat))
     Vle_coordinates.append(float(long))

     Village_Name = list(df["Village Name"])
     Lats = list(df["Latitude"])
     Longs = list(df["Longitude"])
     Population = list(df['Village Population'])

     temp = list(zip(Lats,Longs))
     villages= dict((key,value) for key,value in zip(Village_Name,temp))
     distance =[]

     for key,values in villages.items():
        d = (GD(Vle_coordinates,values).km)
        distance.append(round(d,2))

     Vle_details = list(zip(Village_Name,distance,Population))

     s = sorted(Vle_details, key = lambda x: (x[1], -x[2]))

     final = []

     for items in s:
        if (items[1]<=float(rad)):
            final.append(items[0])


     return render(request,'home.html',{'data1':final})
    except Exception as e:

     print(e)
     
    

