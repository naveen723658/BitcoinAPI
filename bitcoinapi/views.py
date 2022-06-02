from django.views import View
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from.forms import signin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import json, requests
from . models import bitcoin
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets , mixins
from . serializers import bitcoinSerializer
from rest_framework.response import Response

# function for registeration
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            sf = signin(request.POST)
            if sf.is_valid():
                sf.save()
                messages.success(request, 'User created Successfully.')
        else:
            sf = signin()
        return render(request, 'login.html', {'form': sf})
    else:
        return HttpResponseRedirect('/')

# function for login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login succesfully')
                    return HttpResponseRedirect('/signup/')
        else:
            fm = AuthenticationForm()
        return render(request, 'loginform.html', {'lform': fm})
    else:
        return HttpResponseRedirect('/')

# function for logout
def user_logout(request):
    logout(request)
    messages.info(request, 'Logout successfully')
    return HttpResponseRedirect('/login/')


# function for fetching bitcoin prices
class bitcoindata(View):
    response_API = requests.get('https://api.nomics.com/v1/currencies/ticker?key=d750184f059aedf09b9277a4620f4c88338f3cf4&interval=1d,30d&ids=BTC&convert=INR&.json')
    data = response_API.text
    parse_json = json.loads(data)
    for dic in parse_json:
        b_price = dic.get('price')
        b_timestamp = dic.get('price_timestamp')

    bitcoin_data = {
        'price': b_price,
    }
    # Every time the price of bitcoin is fetched it is stored in a database table
    bitcoin_item = bitcoin.objects.create(**bitcoin_data)
    bitcoin_item.save()

    def get(self, request):
        items_count = bitcoin.objects.count()
        messages = "data fatch successfully"
        data = {
            'message': messages,
            'count': items_count,
        }

        return JsonResponse(data)

# function for viewing list of Bitcoin prices (With timestamps with pagination, 10 items per page)
class bitcoinViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, LoginRequiredMixin, viewsets.GenericViewSet):
    login_url = '/login/'
    redirect_field_name = 'login'
    queryset = bitcoin.objects.all()
    serializer_class = bitcoinSerializer

    
