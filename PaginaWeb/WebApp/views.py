from asyncore import read
from django.shortcuts import render
from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from WebApp.models import Prueba


def test(request):
    return render(request, 'WebApp/index.html')

