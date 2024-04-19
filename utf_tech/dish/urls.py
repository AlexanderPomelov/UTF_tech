from django.urls import path
from .views import FoodView

app_name = 'dish'

urlpatterns = [
    path('foods', FoodView.as_view(), name='foods'),
]
