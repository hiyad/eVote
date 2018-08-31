from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^voters/$', views.UserList.as_view()),
    url(r'^voters/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
