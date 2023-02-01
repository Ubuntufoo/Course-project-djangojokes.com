from django.urls import path
from .views import (JokeCreateView, JokeListView, JokeDeleteView,
                    JokeDetailView,  JokeUpdateView)

app_name = 'jokes'
urlpatterns = [
    path('joke/<int:pk>/update/', JokeUpdateView.as_view(), name='update'),
    path('joke/<int:pk>/delete/', JokeDeleteView.as_view(), name='delete'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
    path('', JokeListView.as_view(), name='list'),
]
