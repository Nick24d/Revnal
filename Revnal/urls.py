"""
URL configuration for Revnal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from codereviews.views import code_review_list, code_review_detail, review_update
from inboxjournal.views import journal_public_list, journal_detail, journal_login, journal_dashboard
from .views import postmark_webhookview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook/inbound/', name="webhook", view=postmark_webhookview),
    path('', journal_login, name='journal_login'),
    path('login/', journal_login, name='journal_login'),
    path('dashboard/', journal_dashboard, name='journal_dashboard'),
    path('entry/<int:pk>/', journal_detail, name='journal_detail'),
    path('public_journal/', journal_public_list, name='journal_public_list'),
    path('reviews/', code_review_list, name='codereview_list'),
    path('reviews/<int:pk>/', code_review_detail, name='review_detail'),
    path('reviews/update/<int:pk>/', review_update, name='review_update'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)