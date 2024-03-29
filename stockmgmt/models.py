
from django.db import models

category_choice = (
		('Furniture', 'Furniture'),
		('IT Equipment', 'IT Equipment'),
		('Phone', 'Phone'),
	)

# Create your models here.
class Stock(models.Model):
   category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice)
   item_name = models.CharField(max_length=50, blank=True, null=True)
   quantity = models.IntegerField(default='0', blank=True, null=True)
   recieve_quantity = models.IntegerField(default='0', blank=True, null=True)
   receive_by = models.CharField(max_length=50, blank=True, null=True)
   issue_by = models.CharField(max_length=50, blank=True, null=True)
   issue_to = models.CharField(max_length=50, blank=True, null=True)
   issue_quantity = models.IntegerField(default='0', blank=True, null=True)
   phone_number = models.IntegerField(default='0', blank=True, null=True)
   created_by = models.CharField(max_length=50, blank=True, null=True)
   reorder_level = models.IntegerField(default='0', blank=True, null=True)
   last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
   export_to_CSV = models.BooleanField(default=False)

   def __str__(self):
       return self.item_name + ' ' + str(self.quantity)