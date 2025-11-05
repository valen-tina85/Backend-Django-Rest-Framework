from rest_framework.routers import DefaultRouter
from .views import CalificacionViewSet, MercadoViewSet, OrigenViewSet

router = DefaultRouter()
router.register(r'calificaciones', CalificacionViewSet)
router.register(r'mercado', MercadoViewSet)
router.register(r'origen', OrigenViewSet)

urlpatterns = router.urls
