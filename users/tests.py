from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('habits:habit-list-create')
        data = {
            'user': self.user.id,
            'place': 'дома',
            'time': '12:00:00',
            'action': 'делать зарядку',
            'is_pleasurable': True,
            'frequency': 1,
            'estimated_time': 30,
            'is public': False,
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Исправлено: Ожидается HTTP 201 CREATED
        self.assertEqual(Habit.objects.count(), 1)

    def test_read_habit_list(self):
        Habit.objects.create(user=self.user, place='дома', time='12:00:00', action='делать зарядку', is_pleasurable=True, frequency=1, estimated_time=30)
        url = reverse('habits:habit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_update_habit(self):
        habit = Habit.objects.create(user=self.user, place='дома', time='12:00:00', action='делать зарядку', is_pleasurable=True, frequency=1, estimated_time=30)
        url = reverse('habits:habit-detail', kwargs={'pk': habit.pk})
        data = {'place': 'спортзал', 'time': '15:00:00', 'action': 'плавать', 'is_pleasurable': True, 'frequency': 2, 'estimated_time': 45}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.place, 'спортзал')
        self.assertEqual(habit.time.strftime('%H:%M:%S'), '15:00:00')
        self.assertEqual(habit.action, 'плавать')
        self.assertEqual(habit.frequency, 2)
        self.assertEqual(habit.estimated_time, 45)
