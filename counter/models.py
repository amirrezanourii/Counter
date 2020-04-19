from django.db import models

class Count(models.Model):
    mid_number = models.IntegerField()

    def __str__(self):
        return "{}".format(str(self.mid_number))
    

    
    
