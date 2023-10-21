from django.urls import path, include   

urlpatterns = [
    path('', include('ep.urls')),
]
