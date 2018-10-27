
from django.conf.urls import url

from . import views
urlpatterns = [
    url('add_urls/', views.ExtractUrls.as_view()),
    ]
