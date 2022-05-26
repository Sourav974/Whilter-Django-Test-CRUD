"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from api.views import *
from component.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-component/', GetComponents.as_view()),
    path('create-component/', CreateComponents.as_view()),
    path('update-component/', UpdateComponents.as_view()),
    path('delete-component/', DeleteComponents.as_view()),
    path('get-components/', GetComponents1.as_view()),
    path('create-components/', CreateComponents1.as_view()),
    path('update-components/', UpdateComponents1.as_view()),
    path('delete-components/', DeleteComponents.as_view()),
    path('get-componentid/', GetComponentId.as_view()),

]
