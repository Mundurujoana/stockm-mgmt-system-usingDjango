from pyexpat import model
from django.contrib import admin


# Register your models here.
from .forms import StockcreateForm
from .models import Stock

class StockCreateAdmin(admin.ModelAdmin):
    list_display =['category', 'item_name', 'quantity']
    form = StockcreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']

admin.site.register(Stock, StockCreateAdmin)