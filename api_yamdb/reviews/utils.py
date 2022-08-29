from rest_framework import serializers

from django.utils import timezone


def validate_year(value):

    current_year = timezone.now().year
    if not 0 <= value <= current_year:
        raise serializers.ValidationError(
            'Укажите год создания произведения.'
        )
    return value


def validate_username(self, value):
    """Проверяем, пытается ли пользователь
        использовать "me" в качестве имени пользователя"""
    if value.lower() == 'me':
        raise serializers.ValidationError("Недопустимое имя пользователя")
    return value
