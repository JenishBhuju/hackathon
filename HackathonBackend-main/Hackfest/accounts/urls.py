from django.urls import path
from . import views

from . import views

urlpatterns = [
    # path('/createnurse/', views.addNurse),
    # path('/createdoctor/', views.addDoctor),
    # path('/checkusercheck/<roledata>' ,views.doctor_register),
    # path('/loginpage' , views.docter_login),
    # path('/logout' , views.doctor_logout),
    # path('/choise/', views.choiseview)
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]