"""
URL configuration for Powerlook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls),
    path("" , views.index, name='home'),
    path("about", views.about , name ='about'),
    path("store", views.store, name="store"),
    path("order", views.order, name="order"),
    path("product", views.product, name='product'),
    path("login", views.login, name= "login" ),
    path("signup", views.signup, name= "signup"),
    path("cart", views.view_cart, name="cart"),
    path("add_cart", views.add_cart, name= "add_cart"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)