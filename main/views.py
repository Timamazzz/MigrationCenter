from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'dist/index.html')


def redirect_from_root(request):
    return redirect(to='/main/')
