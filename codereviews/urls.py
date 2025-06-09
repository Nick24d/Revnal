from django.urls import path

from inboxjournal.urls import app_name
from . import views

app_name = 'codereviews'

urlpatterns = [
    path('', views.code_review_list, name='codereview_list'),
    path('review/<int:pk>/', views.code_review_detail, name='review_detail'),
]
