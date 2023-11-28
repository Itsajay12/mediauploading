from django.shortcuts import render,redirect
from .forms import*
from .models import*
# Create your views here.
def index(request):
    form=bookform()
    if request.method=="POST":
        form=bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(list_data)
    return render(request,'page1.html',{"form":form})
def list_data(request):
    query=Book.objects.all()
    return render(request,'page2.html',{"query":query})