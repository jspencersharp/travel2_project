from django.conf.urls import url, include
from . import views

def test(request):
    print """

            This is the app level URL tester......   



            """

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]