from django.conf.urls import url
from . import views
def test(request):
    print """


    This is the main_project APP  level URL tester


    """
urlpatterns = [
    url(r'^dashboard/$', views.dashboard),
    url(r'^addTrip/$', views.addTrip),
    url(r'^createTrip/$', views.createTrip),
    url(r'^show/(?P<id>\d+)/$', views.show),
    url(r'^link/(?P<id>\d+)/$', views.link),
]