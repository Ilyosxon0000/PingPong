from django.urls import path,include
from rest_framework.routers import DefaultRouter
from webapp.views import TableViewSet,OrderViewSet,TableLogViewSet

router=DefaultRouter()
router.register('tables',TableViewSet)
router.register('orders',OrderViewSet)
router.register('table-logs',TableLogViewSet)

urlpatterns=[
    path("",include(router.urls))
]