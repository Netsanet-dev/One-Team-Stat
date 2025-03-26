from django.urls import path
from . import views

urlpatterns =[
    
    path('api/register/', views.register_user, name='register'),
    path('api/login/', views.login_user, name='login'),
    path('api/logout/', views.logout_user, name="logout"),
    path('api/update_info/', views.update_user_info, name="update_info"),    
    path('api/protected/', views.protected_view, name="protected"),
    path("api/update_password/", views.update_password, name='update-password')
]
