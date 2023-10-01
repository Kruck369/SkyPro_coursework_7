from rest_framework import generics
from .models import Habit
from .paginators import HabitPaginator
from .serializers import HabitSerializer
from .permissions import IsOwnerOrReadOnly
from .tasks import send_notification


class HabitListCreateAPIView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        habit = serializer.instance
        user_id = self.request.user.telegram_user_id
        message = f"Пора выполнить вашу привычку: {habit.action} в {habit.time} {habit.place}"
        send_notification.apply_async(args=[user_id, message], eta=habit.time)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrReadOnly]
