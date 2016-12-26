from django.conf.urls import url

from .views import Create

urlpatterns = [
    url(r'^$', Create.as_view()),
]
