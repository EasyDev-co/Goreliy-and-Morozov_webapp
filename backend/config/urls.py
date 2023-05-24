from django.contrib import admin
from django.urls import path, include

from .swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
