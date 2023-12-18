# import rest_framework
from rest_framework import status,permissions,viewsets,response
# import local models
from webapp.models import Table,Order,TableLog
# import local serializers
from webapp.serializers import TableSerializer,OrderSerializer,TableLogSerializer
# Create your views here.

class TableViewSet(viewsets.ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=TableSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class TableLogViewSet(viewsets.ModelViewSet):
    queryset=TableLog.objects.all()
    serializer_class=TableLogSerializer