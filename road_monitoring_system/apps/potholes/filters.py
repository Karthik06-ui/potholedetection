import  django_filters
from .models import PotholeEvent


class PotholeEventFilter(django_filters.FilterSet):
    severity = django_filters.ChoiceFilter(choices=PotholeEvent.SEVERITY_CHOICES)
    created_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = PotholeEvent
        fields = ['severity', 'created_after', 'created_before']