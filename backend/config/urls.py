from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('graphql/', include('sample.urls')),
    path('admin/', admin.site.urls),
]
