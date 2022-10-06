from django.urls import path
from . import views


urlpatterns = [
    path('set_session', views.set_session, name = 'set_session'),
    path('get_session', views.get_session, name = 'get_session'),
    path('del_session', views.del_session, name = 'del_session')
]