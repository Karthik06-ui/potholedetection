from django.db import models


class PotholeEvent(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    SEVERITY_COLOR_MAP = {
        'low': 'green',
        'medium': 'orange',
        'high': 'red',
    }

    latitude = models.FloatField()
    longitude = models.FloatField()
    vibration_value = models.FloatField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, blank=True)
    image = models.ImageField(upload_to='potholes/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    color=property(lambda self: self.SEVERITY_COLOR_MAP.get(self.severity, 'gray'))
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Pothole Event'
        verbose_name_plural = 'Pothole Events'

    def __str__(self):
        return f"[{self.severity.upper()}] ({self.latitude}, {self.longitude}) @ {self.created_at:%Y-%m-%d %H:%M}"