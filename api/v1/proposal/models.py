from django.db import models

from api.v1.utilis.enums import ObjectStatus


class Proposal(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=ObjectStatus.choices(), default=ObjectStatus.new)


    def __str__(self):
        return self.phone_number
    
