from django.core.exceptions import ValidationError
from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=255, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_pleasurable = models.BooleanField(default=False, verbose_name='приятная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='связанная привычка')
    frequency = models.PositiveIntegerField(default=1, verbose_name='частота')
    reward = models.CharField(max_length=255, null=True, blank=True, verbose_name='награда')
    estimated_time = models.PositiveIntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='публичная')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def save(self, *args, **kwargs):
        if self.related_habit and not self.related_habit.is_pleasurable:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        super(Habit, self).save(*args, **kwargs)
