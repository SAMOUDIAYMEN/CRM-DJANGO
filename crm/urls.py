from django.urls import path
from django.contrib.auth import views as auth_views
from crm.views import project, customer, profile, createProject, updateProject, deleteProject, createCustomer, updateCustomer, deleteCustomer, createProfile, updateProfile, deleteProfile,register_request,login_request,logout_request,task, createTask, updateTask, deleteTask, profilePage

from . import views

urlpatterns = [
    path('Project/', project, name='project'),
    path('create-Project/', createProject, name='create-Project'),
    path('update-Project/<str:pk>/', updateProject, name='update-Project'),
    path('delete-Project/<str:pk>/', deleteProject, name='delete-Project'),

    path('Task/', task, name='task'),
    path('create-Task/', createTask, name='create-Task'),
    path('update-Task/<str:pk>/', updateTask, name='update-Task'),
    path('delete-Task/<str:pk>/', deleteTask, name='delete-Task'),

    path('customer/', customer, name='customer'),
    path('create-customer/', createCustomer, name='create-customer'),
    path('update-customer/<str:pk>/', updateCustomer, name='update-customer'),
    path('delete-customer/<str:pk>/', deleteCustomer, name='delete-customer'),

    path('profile/', profile, name='profile'),
    path('create-profile/', createProfile, name='create-profile'),
    path('update-profile/<str:pk>/', updateProfile, name='update-profile'),
    path('delete-profile/<str:pk>/', deleteProfile, name='delete-profile'),

    path("profile-page", profilePage, name="profile-page"),

    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='crm/change_password.html'), name='password-change'),

    #path('task/', task, name='customer'),
    #path('create-task/', createTask, name='create-task'),
    #path('update-task/<str:pk>/', updateTask, name='update-task'),
    #path('delete-task/<str:pk>/', deleteTask, name='delete-task'),

    #path('Profile/', ),
    #path('register/', ),
    
]