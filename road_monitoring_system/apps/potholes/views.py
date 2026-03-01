from rest_framework import viewsets, mixins, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.shortcuts import render
from .models import PotholeEvent
from .serializers import PotholeEventSerializer
from .services import create_pothole_event


class PotholeEventViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = PotholeEvent.objects.all()
    serializer_class = PotholeEventSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = create_pothole_event(serializer.validated_data)
        output = self.get_serializer(instance)
        return Response(output.data, status=status.HTTP_201_CREATED)
    
def dashboard(request):
    events = PotholeEvent.objects.all()

    severity_counts = {
        'low': events.filter(severity='low').count(),
        'medium': events.filter(severity='medium').count(),
        'high': events.filter(severity='high').count(),
    }

    context = {
        'events': events[:50],
        'total': events.count(),
        'severity_counts': severity_counts,
        'map_points': [
            {
                'lat': e.latitude,
                'lng': e.longitude,
                'severity': e.severity,
                'vibration': e.vibration_value,
                'color': e.color,
                'created_at': e.created_at.strftime('%Y-%m-%d %H:%M'),
            }
            for e in events
        ],
    }
    return render(request, 'potholes/dashboard.html', context)