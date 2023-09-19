from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def reservation_list(request):
    return  HttpResponse('This is page for manager')