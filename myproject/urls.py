from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gui.urls')),  # Replace 'myapp' with the name of your app
]
