from django.db import models

class ExchangeRate(models.Model):
    date = models.DateField()
    currency = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.CharField(max_length=100, default='BCM')
    
    class Meta:
        ordering = ['-date']
        unique_together = ['date', 'currency']
    
    def __str__(self):
        return f"{self.currency} - {self.date}: {self.rate}"