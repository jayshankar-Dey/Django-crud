from django.shortcuts import redirect, render
from .forms import Register
from . models import user

# this function add itom show itom
def home(request):
    if request.method == 'POST':
        fm = Register(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Register()
    else:
        fm = Register(request.POST)
    
    users = user.objects.all()
    return render(request,'home.html',{'form':fm,'user':users})
#this function delete data

def delete(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return redirect('http://127.0.0.1:8000/home/')
    
#updet function
def updet(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = Register(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
           
           pi = user.objects.get(pk=id)
           fm = Register( instance=pi)

        return render(request,'updet.html',{'form':fm})
