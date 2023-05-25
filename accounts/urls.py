from django.urls import path
from .views import Signup, Login, Logout


app_name = 'accounts'
urlpatterns = [
    path('singup/', Signup, name='signup'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
]