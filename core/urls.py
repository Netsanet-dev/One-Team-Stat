from django.urls import path
from . import views

urlpatterns =[
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('update_info/', views.update_user_info, name="update_info"),    
    path('update_password/', views.update_password, name='update-password'),
    path('protected/', views.protected_view, name="protected"),
    path('refresh_token/', views.refresh_token_view, name="refresh-token"),
]
