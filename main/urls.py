from django.urls import path
from . import views
#from .views import registration

urlpatterns = [
path("", views.index, name="index"),
path("home/", views.home, name="home"),
path("signup/", views.signup, name="signup"),
path("registration/", views.registration, name="registration"),
path("successPage/", views.successpage, name="successpage"),
path("successPageTwo/", views.successpagetwo, name="successpagetwo"),
path("logout/", views.logout, name="logout"),
]

#start/