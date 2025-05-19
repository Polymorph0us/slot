from django.contrib import admin
from django.urls import path
from timetable.views import timetable_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timetable/', timetable_view, name='timetable'),
]
