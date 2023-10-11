from django.shortcuts import render, redirect
from .models import Band
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    """
        Render the home page.

        This view renders the 'home.html' template, representing the home page of the website.

        Args:
        request (HttpRequest): The request object.

        Returns:
        HttpResponse: The response to be rendered as the home page.
        """
    return render(request, 'home.html')


@login_required
def about(request):
    """
        Render the about page with login required.

        This view renders the 'about.html' template, representing the about page of the website.
        A user must be logged in to access this view.

        Args:
        request (HttpRequest): The request object.

        Returns:
        HttpResponse: The response to be rendered as the about page.
        """
    return render(request, 'about.html')


@login_required
def band(request):
    """
        Render the band page with login required.

        This view retrieves a list of bands from the database and renders the 'band.html' template.
        A user must be logged in to access this view.

        Args:
        request (HttpRequest): The request object.

        Returns:
        HttpResponse: The response to be rendered as the band page.
        """
    bands = Band.objects.all()
    return render(request, 'band.html', {'bands': bands})


def register(request):
    """
        User registration view.

        This view handles user registration using the Django UserCreationForm.
        If the request method is POST and the form is valid, a new user is created, and they are logged in.
        If the method is GET or the form is not valid, the registration form is displayed.

        Args:
        request (HttpRequest): The request object.

        Returns:
        HttpResponse: The response to be rendered, which can be the registration form or a redirection to the band page upon successful registration.
        """
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
