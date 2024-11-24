from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('edit/<int:topic_id>/', views.edit, name='edit'),
    path('delete/<int:topic_id>/', views.delete, name='delete'),
]