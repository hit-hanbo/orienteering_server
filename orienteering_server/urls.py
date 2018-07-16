"""orienteering_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from server.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login/', user_login),
    path('user/register/', user_register),
    path('user/logout/', user_logout),
    path('user/query/', user_query),
    path('user/activities/', user_activity_list),
    path('activity/create/', activity_add),
    path('activity/part/', activity_part),
    path('activity/query/', activity_query),
    path('activity/list/', activity_list),
]
