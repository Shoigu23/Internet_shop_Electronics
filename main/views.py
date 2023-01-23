from django.shortcuts import render
# from django.http import HttpResponseRedirect
from main.models import Product

# Create your views here.
def main(request):
    pr = Product.objects.all()
    return render(request, 'index.html',{'pr':pr})
