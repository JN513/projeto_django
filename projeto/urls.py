"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core.views import (
    home,
    post,
    criar_post,
    login,
    logout,
    cadastro,
    editar_post,
    deletar_post,
    user,
)

urlpatterns = (
        [
        path("admin/", admin.site.urls, name="admin"),
        path("", home, name="home"),
        path("post/<int:id>/", post, name="post"),
        path("criar/post/", criar_post, name="criar_post"),
        path("login/", login, name="login"),
        path("logout/", logout, name="logout"),
        path("cadastro/", cadastro, name="cadastro"),
        path("editar/post/", editar_post, name="editar_post"),
        path("deletar/post/", deletar_post, name="deletar_post"),
        path("user/<int:id>/", user, name="user")
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
