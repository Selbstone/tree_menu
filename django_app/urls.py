from django.conf.urls import url
from django.views.generic import TemplateView
from django_app.views import IndexView

app_name = 'django_app'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='test'),
    url(r'^(.*)/$', IndexView.as_view(), name='test'),
]
