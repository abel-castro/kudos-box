"""kudosbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from boxes.views import (BoxCreateView, BoxDetailView, BoxUserCreateView,
                         HomeView, MessageCreateView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"", HomeView.as_view(), name="home"),
    path(r"boxes/create/", BoxCreateView.as_view(), name="box_create"),
    path(r"boxes/<slug:slug>/", BoxDetailView.as_view(), name="box_detail"),
    path(
        r"boxes/<slug:slug>/create-user/",
        BoxUserCreateView.as_view(),
        name="create_box_user",
    ),
    path(
        r"boxes/<slug:slug>/create-message/",
        MessageCreateView.as_view(),
        name="message_create",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
