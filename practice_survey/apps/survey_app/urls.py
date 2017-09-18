from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.survey),
    url(r'^surveys/process$', views.process),
    url(r'^result$', views.result),
]