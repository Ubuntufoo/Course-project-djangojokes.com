from django.urls import path
from .views import JokeListView, JokeDetailView

app_name = 'jokes'
urlpatterns = [
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
    path('', JokeListView.as_view(), name='list'),
]
