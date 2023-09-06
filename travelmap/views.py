from django.shortcuts import render

def travelmap(request):
    return render(request, 'travelmap/map.html')
