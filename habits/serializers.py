from rest_framework import serializers
from .models import Habit
from .validators import FrequencyValidator, RelatedHabitAndRewardValidator, TimeValidator, PleasurableValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            FrequencyValidator(field='frequency'),
            RelatedHabitAndRewardValidator(field_1='related_habit', field_2='reward'),
            TimeValidator(field='estimated_time'),
            PleasurableValidator(field_1='is_pleasurable', field_2='reward', field_3='related_habit')
        ]
