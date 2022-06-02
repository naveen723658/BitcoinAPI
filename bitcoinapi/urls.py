from django.urls import path, include
from . import views
from . views import bitcoinViewSet , bitcoindata, signup, user_login, user_logout
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bitcoin', bitcoinViewSet)

urlpatterns = [
    path('', include(router.urls), name='home'),
    path('bitcoinfatch/', bitcoindata.as_view()),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]