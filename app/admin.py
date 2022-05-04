from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product


@admin.register(Product)
class ProductModelAdmin(ImportExportModelAdmin):
	...
