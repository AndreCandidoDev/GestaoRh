from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'core/index.html')
