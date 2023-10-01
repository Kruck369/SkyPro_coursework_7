from django.urls import path
from .views import HabitListCreateAPIView, HabitDetailAPIView, HabitListAPIView, PublicHabitListAPIView


from habits.apps import HabitsConfig


app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habit-list'),
    path('habits/public/', PublicHabitListAPIView.as_view(), name='habit-public-list'),
    path('habits/create/', HabitListCreateAPIView.as_view(), name='habit-list-create'),
    path('habits/<int:pk>/', HabitDetailAPIView.as_view(), name='habit-detail'),
]
