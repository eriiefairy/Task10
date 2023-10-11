from django.shortcuts import render, redirect
from .models import Band
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def band(request):
    bands = Band.objects.all()
    return render(request, 'band.html', {'bands': bands})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('band')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


#def login(request):
  #  return render(request, 'login.html')
