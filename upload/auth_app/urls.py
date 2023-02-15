from django.urls import path
from .views import register_view,login_view,logout_view


urlpatterns = [
    path('rv/',register_view,name='signup_url'),
    path('lv/',login_view,name='signin_url'),
    path('lgv/',logout_view,name='signout_url')
]
