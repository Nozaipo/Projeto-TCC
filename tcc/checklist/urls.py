from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checklist, name="checklist"),
    path('save_record', views.save_record, name="save_record"),
    # path('login', views.web_login, name="login"),
    path('check_user', views.check_user, name="check_user"),
    path('accounts/', include('django.contrib.auth.urls')),
]