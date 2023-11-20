from django.urls import path
from . import views
from .views import (
    DestinationDetailView
)

app_name = 'myapp'

urlpatterns = [
    # path('', views.home_page, name = 'visitor home page'), #default homepage
    path('', views.home_page_logged_in, name = 'home page'),
    # path('logged-in', views.home_page_logged_in, name = 'user home page'),
    path('register', views.register, name = 'register'),
    path('sign-in', views.sign_in, name = 'sign-in'),
    path('login', views.login, name = 'login'),
    # path('logout', views.logout, name = 'logout'),
    path('log_out', views.log_out, name = 'logout'),
    path('feedback', views.display_feedback, name = 'display feedback'),
    path('create-feedback', views.create_feedback, name = 'create feedback'),
    path('check-delete', views.check_delete, name = 'check delete'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('individual-feedback/<str:pk>', views.individual_feedback, name='individual feedback'),
    path('destinations/<slug>/', DestinationDetailView.as_view(), name = 'destinations'),
    # path('test-destination', views.test_destinations, name = 'destinations')
  ]