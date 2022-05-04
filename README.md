# Django filter

## Installation

```bash
pip install django-filter
```

then added it to the installed apps

```python
INSTALLED_APPS = [
   ...
   'django_filters',
   ...
]
```

## Writing filter classes

Let't consider the following model

```python
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()


```

To create a filter classes for this model, first create a new file `filters.py` (optional) then add to it the following code

```python
# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
    release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')

    class Meta:
        model = Product
        fields = []


```

This following filter class will give the ability to filter products by price (this will filter using price__iexact) and price__gt and price__lt, the release_year, release__year__gt and release__year__lt.

Now we create a serializer for the product model, create a new file `serializers.py` and add the following code to it.

```python
# serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


```

finally we create a view for getting the products, in `views.py` add the following code

```python
# views.py
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


```


