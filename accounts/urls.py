from cProfile import Profile
from django.urls import path

from .views import SignUpView, HomeView, DashboardView, ProfileView, ProfileUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    
   
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),




]
