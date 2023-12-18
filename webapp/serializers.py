from rest_framework import serializers
from webapp.models import Table,Order,TableLog

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
    
    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request", None)
        if request and request.method == "GET":
            order_table=request.GET.get("order_table")
            if order_table:
                self.fields["table"] = TableSerializer(context=self.context)
    

class TableLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=TableLog
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(TableLogSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request", None)
        if request and request.method == "GET":
            logs_table=request.GET.get("logs_table")
            if logs_table:
                self.fields["table"] = TableSerializer(context=self.context)