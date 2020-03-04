from django.urls import path
from .views import PfolioList, about_view, contact_view, home_view 
from django.conf.urls import url

urlpatterns = [
    url('', PfolioList.as_view(),name='pfolios'),
    url(r'^about/$', about_view, name="about"),
    url(r'^contact/$', contact_view, name="contact"),
    url(r'^$', home_view, name="home")
]
