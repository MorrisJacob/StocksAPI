import requests
import json
from stocks import settings

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        token = settings.FINNHUB_API_KEY
        r = requests.get(
                "https://finnhub.io/api/v1/stock/symbol?exchange=US&token=" +
                token)

        json = r.json()

        return render(request, 'index.html', { 'data': json })

class SingleStockPageView(TemplateView):
    def get(self, request, **kwargs):
        token = settings.FINNHUB_API_KEY
        stock = request.GET.get('stock')
        stock_name = request.GET.get('name')
        r = requests.get(
                'https://finnhub.io/api/v1/stock/recommendation?symbol=' +
                stock + '&token=' + token)

        stock_data = r.json()

        ctx = { 'data': stock_data, 'stock_name': stock_name }

        return render(request, 'single_stocks.html', ctx)
