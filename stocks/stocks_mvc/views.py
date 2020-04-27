import requests
import json
from stocks import settings

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        token = settings.FINNHUB_API_KEY
        r = requests.get(
                'https://finnhub.io/api/v1/stock/exchange?token=' + token)

        print(token)
        json = r.json()

        return render(request, 'index.html', { 'data': json })
