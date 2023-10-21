from django.db import models
from django.utils import timezone

# Create your models here.
class Risk(models.Model):
    risk_name = models.CharField(max_length=100)
    frequency_occurrence = models.IntegerField()
    severity_occurrence = models.IntegerField()
    chance_detection = models.IntegerField()
    active = models.BooleanField(default=1)
    date_creation = models.DateField(default=timezone.now)
    action_plan = models.JSONField(null=True)
    contingency_measures = models.JSONField(null=True)

    def __str__(self):
        return self.risk_name

    def get_risk_name(self):
        return self.risk_name
    
    def get_risk_property(self):
        return {self.risk_name: {"FO": self.frequency_occurrence,"SO": self.severity_occurrence, "CD": self.chance_detection}}
    
    def get_date_creation(self):
        return self.date_creation
    
class Form(models.Model):
    risks_observed = models.ManyToManyField(Risk, related_name='risks_observed')
    who_applied = models.CharField(max_length=100)
    date_creation = models.DateField(default=timezone.now)
    observations = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.who_applied
