from . import views
from django.urls import path


app_name = 'lesson4'

urlpatterns = [
    path('', views.get_context_data, name='index'),
    path('insert/', views.insert_form, name='good_create'),
]
