# core/urls.py
from rest_framework.routers import DefaultRouter
from .views import AreaViewSet, PlatilloViewSet, PedidoViewSet, ParteViewSet

router = DefaultRouter()
router.register(r'areas', AreaViewSet)
router.register(r'platillos', PlatilloViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'partes', ParteViewSet)

urlpatterns = router.urls
