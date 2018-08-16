from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.
@login_required
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'principal/index.html')

def logout_view(request):
    logout(request)
    return redirect('/')
