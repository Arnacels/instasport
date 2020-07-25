from django.conf.urls import url
from .views import TimeTableListView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^timetablelist/$', TimeTableListView.as_view(), name='timetablelist'),
]

urlpatterns = format_suffix_patterns(urlpatterns)