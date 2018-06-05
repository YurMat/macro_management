from django.conf.urls import url

from . import views

app_name = 'nutrient'
urlpatterns = [
    url('calendar/', views.calendar, name='calendar'),
    url('daily_intake/', views.daily_intake, name='daily_intake'),
    url('daily_intake_edit/', views.daily_intake_edit, name='daily_intake_edit'),
]