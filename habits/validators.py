from rest_framework.validators import ValidationError


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value > 7:
            raise ValidationError('Привычку нельзя выполнять реже, чем 1 раз в 7 дней.')


class RelatedHabitAndRewardValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, data):
        tmp_value_1 = data.get(self.field_1)
        tmp_value_2 = data.get(self.field_2)
        if tmp_value_1 and tmp_value_2:
            raise ValidationError('Привычка не может иметь и связанную привычку, и вознаграждение одновременно.')


class TimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value > 120:
            raise ValidationError('Время выполнения не должно превышать 120 секунд.')


class PleasurableValidator:
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, data):
        tmp_value_1 = data.get(self.field_1)
        tmp_value_2 = data.get(self.field_2)
        tmp_value_3 = data.get(self.field_3)
        if tmp_value_1 and (tmp_value_2 or tmp_value_3):
            raise ValidationError('Приятная привычка не должна иметь вознаграждения или связанной привычки.')
