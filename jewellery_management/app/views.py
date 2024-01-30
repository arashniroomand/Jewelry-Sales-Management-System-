from django.shortcuts import render
from .models import *
# Create your views here.
def JewelleryView(request):
    get_jewellery = Jewellery.objects.all()
    context = {
        "get_jewellery" : get_jewellery
    }
    return render(request, 'app/jewellery.html',context)