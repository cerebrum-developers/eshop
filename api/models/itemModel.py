from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
import datetime

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    cost_price = models.FloatField(default=0.00)
    selling_price = models.FloatField(default=0.00)
    sale_tax = models.BooleanField(default=False)
    stock = models.FloatField(default=0)
    expiry_date = models.DateField(blank=True)
    batch_number = models.FloatField(default=0)
    # measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    deleted_at = models.DateTimeField(blank=True, null=True)

    history = HistoricalRecords(table_name='item_history')

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = 'item'
        indexes = [
            models.Index(fields=['id', 'item_name'])
        ]
