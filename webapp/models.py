from django.db import models

# Create your models here.

class Table(models.Model):
    STATUS=(
        ("Band","Band"),
        ("Bo'sh","Bo'sh")
    )
    name=models.CharField(max_length=255)
    price=models.IntegerField(default=0)
    status=models.CharField(max_length=10,choices=STATUS,default="Bo'sh")

class Order(models.Model):
    table=models.ForeignKey(Table,related_name="orders",on_delete=models.PROTECT)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    description=models.TextField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    changed_date=models.DateTimeField(auto_now=True)
    # TODO user informations
class TableLog(models.Model):
    table=models.ForeignKey(Table,related_name="table_logs",on_delete=models.PROTECT)
    start_time=models.TimeField()
    end_time=models.TimeField()
    total_price=models.IntegerField(default=0)
    description=models.TextField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    changed_date=models.DateTimeField(auto_now=True)

    def get_total_price(self):
        total_hour=self.start_time.hour-self.end_time.hour


