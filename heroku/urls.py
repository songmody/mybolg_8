
from django.contrib import admin
from django.urls import path
import herokuapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',herokuapp.views.home),
]
