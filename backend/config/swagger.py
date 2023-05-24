from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Goreliy & Morozov",
        default_version="v1",
        description="API.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="HS.Kazakov@mail.ru"),
        license=openapi.License(name="BSD-3")
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)
