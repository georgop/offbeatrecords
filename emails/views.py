from django.shortcuts import render,redirect
from .models import info
from .forms import EmailForm
def index(request):
    return render(request,'emails/index.html')

def new(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmailForm()
    return render(request,'emails/index.html',{'form': form})