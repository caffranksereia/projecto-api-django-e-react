from django.conf import setting
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from drf_spectacular import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

from rest_framework import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path("",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs"),
        path("doc/",SpectacularRedocView.as_view(url_name="api-schema"), name="api-schema"),
        path(setting.ADMIN_URL, admin.site.urls),
        ] + static(setting.MEDIA_URL, document_root = setting.MEDIA_ROOT)

if setting.DEBBUG:
    urlpatterns +=staticfiles_urlpatterns()

urlpatterns += [
    path("api/token",TokenObtainPairView.as_view(), name="token_obtain_pair" ),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify", TokenVerifyView.as_view(), name="token_verify"),

    path("api/", include("config.api_router")),
    path("api/schema", SpectacularAPIView.as_view(), name="api_schema"),
]
