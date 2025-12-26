from django.http import JsonResponse
from django.urls import path, re_path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from drf_spectacular.settings import spectacular_settings

# Swagger/Redoc Settings
spectacular_settings.SWAGGER_UI_SETTINGS = {
    'title': 'LexiRus - APIs',
    'description': 'LexiRus System - APIs',
    'version': 'v1',
}

# Index Json Response
def root_json_view(request):
    data = {
        "status": True,
        "swagger_ui": "/api/schema/swagger-ui/",
        "message": "Welcome to LexiRus APIs",
        "version": "v1",
        "info": {
            "author": "Damotiva Team",
            "license": "Damotiva License"
        }
    }
    return JsonResponse(data)

urlpatterns = [
    # Index JSON response
    path('', root_json_view, name='root-json'),

    # OpenAPI schema endpoints
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # DRF login/logout
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    # API v1 routes (Lexirus backend)
    path("api/v1/", include("lexirus.urls")),
]
