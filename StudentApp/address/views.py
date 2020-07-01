from django.shortcuts import render
from .models import District

def district_list(request):
    districts = District.objects.all()
    context = {
        'districts': districts
    }
    return render(request, 'address/district_list.html', context)


def district_detail(request, id):
    district = District.objects.get(pk=id)
    context = {
        'district': district
    }
    return render(request, 'address/district_detail.html', context)
