from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.checklist, name="checklist"),
    path('save_record', views.save_record, name="save_record"),
    # path('login', views.web_login, name="login"),
    path('check_user', views.check_user, name="check_user"),
    path('clear', views.clear, name="clear"),
    path('form_history', views.form_history, name='form_history'),
    path('accounts/', include('django.contrib.auth.urls')),
]