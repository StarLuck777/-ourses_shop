from django.contrib import admin
from django.urls import path, include


# api/v1/courses
# api/v1/categories


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('api/', include('api.urls'))
]
