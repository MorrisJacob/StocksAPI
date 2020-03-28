from django.urls import path
from stocks_mvc import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
