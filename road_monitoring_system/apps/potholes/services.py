from .models import PotholeEvent


def calculate_severity(vibration_value: float) -> str:
    if vibration_value < 15:
        return 'low'
    elif vibration_value <= 25:
        return 'medium'
    return 'high'


def create_pothole_event(validated_data: dict) -> PotholeEvent:
    validated_data['severity'] = calculate_severity(validated_data['vibration_value'])
    return PotholeEvent.objects.create(**validated_data)