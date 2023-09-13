from django.db import models

class EODData(models.Model):
    symbol = models.CharField(max_length=10)  # To store the stock symbol like 'TSLA' or 'META'
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adjusted_close = models.FloatField()
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.symbol} - {self.date} - {self.close}"
