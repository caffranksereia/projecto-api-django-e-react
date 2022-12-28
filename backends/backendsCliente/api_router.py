from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apiCliente.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("cadastro", UserViewSet)

app_name = "api"
urlpatterns = router.urls
