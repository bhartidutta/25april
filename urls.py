from django.contrib import admin
from django.urls import path
from .views import djangoform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',djangoform),

]