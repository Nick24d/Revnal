from django.urls import path
from . import views

app_name = 'inboxjournal'

urlpatterns = [
    path('', views.journal_login, name='journal_login'),
    path('login/', views.journal_login, name='journal_login'),
    path('dashboard/', views.journal_dashboard, name='journal_dashboard'),
    path('entry/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('public_journal/', views.journal_public_list, name='journal_public_list'),
]
