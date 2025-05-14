from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
from oauth2_provider.views import TokenView, AuthorizationView
from django.contrib.auth import views as auth_views
from . views import ProtectedView


urlpatterns = [
    path('', views.test),
    path('callback',views.callback,name='callback'),
]+ [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    

]
