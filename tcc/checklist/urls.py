from django.urls import path
from . import views

urlpatterns = [
    path('', views.checklist, name="checklist"),
    path('risks_observed', views.risks_observed, name="risks_observed")
]