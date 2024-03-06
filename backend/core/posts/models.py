from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    variable1 = models.CharField(max_length=50,)  # Use WeekdayField instead of CharField
    variable2 = models.CharField(max_length=50)  # Use WeekdayField instead of CharField
    variable3 = models.CharField(max_length=50)  # Use WeekdayField instead of CharField
    def __str__(self):
        return self.name